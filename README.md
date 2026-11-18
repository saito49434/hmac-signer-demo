# hmac-signer-demo

Webhook HMAC-SHA256 signature verification example

## Quick Start

```bash
python3 -c "import verify_hmac as v; s=v.sign(b'k',b'hi'); print(v.verify(b'k',b'hi',s))"
```

## License

MIT
