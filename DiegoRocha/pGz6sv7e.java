    private static final Charset charset = Charset.forName("Windows-1252");

    private static final ThreadLocal<ByteBuffer> threadBuffer =
            new ThreadLocal<ByteBuffer>()
            {
                protected ByteBuffer initialValue()
                {
                    return ByteBuffer.allocate(256);
                }
            };

    private static final ThreadLocal<CharsetEncoder> threadEncoder =
            new ThreadLocal<CharsetEncoder>()
            {
                protected CharsetEncoder initialValue()
                {
                    return charset.newEncoder()
                            .onUnmappableCharacter(CodingErrorAction.REPORT)
                            .onMalformedInput(CodingErrorAction.REPORT);
                }
            };

    private static final char[] BIN_TO_ASC = {
            '+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8',
            '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    };

    private static byte[] toByteArray(String s, boolean withLen)
    {
        if (s.length() > 255) {
            throw new IllegalArgumentException("String length must be less than 255: " + s.length());
        }
        ByteBuffer buffer = threadBuffer.get();
        CharsetEncoder charsetEncoder = threadEncoder.get().reset();
        buffer.rewind().limit(buffer.capacity());
        if (withLen) {
            buffer.put((byte) s.length());
        }
        CharBuffer in = CharBuffer.wrap(s);
        try {
            CoderResult result = charsetEncoder.encode(in, buffer, true);
            if (!result.isUnderflow()) {
                result.throwException();
            }
            result = charsetEncoder.flush(buffer);
            if (!result.isUnderflow()) {
                result.throwException();
            }
        } catch (CharacterCodingException e) {
            throw new RuntimeException(e);
        }
        buffer.flip();
        byte[] bytes = new byte[buffer.remaining()];
        System.arraycopy(buffer.array(), buffer.arrayOffset(),
                bytes, 0, buffer.remaining());
        return bytes;
    }

    private static String toString(byte[] bytes)
    {
        StringBuilder buf = new StringBuilder(256);
        int len = bytes.length;
        boolean flush = false;
        if (len % 3 != 0) {
            byte[] tmp = new byte[len + 1];
            System.arraycopy(bytes, 0, tmp, 0, len);
            tmp[len++] = 0;
            bytes = tmp;
            flush = true;
        }
        int counter = 0;
        int last = 0;
        for (int i = 0; i < len; i++) {
            int b = i < len ? (bytes[i] & 0xFF) : 0;
            switch (counter) {
                case 0:
                    buf.append(BIN_TO_ASC[b >> 2]);
                    last = b;
                    break;
                case 1:
                    buf.append(BIN_TO_ASC[((last & 0x03) << 4) | ((b & 0xF0) >> 4)]);
                    last = b;
                    break;
                case 2:
                    buf.append(BIN_TO_ASC[((last & 0x0F) << 2) | ((b & 0xC0) >> 6)]);
                    if (!(flush && i == len - 1)) {
                        buf.append(BIN_TO_ASC[b & 0x3F]);
                    }
                    last = 0;
                    break;
                default:
                    throw new AssertionError(counter);
            }
            counter = ++counter % 3;
        }
        return buf.toString();
    }