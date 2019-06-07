import pyrx
import binascii

assert pyrx.__version__ == '0.0.1'

expected = [
        '871a55818ab64ed27bd648a719c4d849c195e7aaebfae343eb06f43659a67430',
        'ec948a8df8a78c1c8612f1236c2914bfddb6aa1db2b1fb2b94af6dc70008c0f2',
        '1a976825cc3925a97245610b00709e00cfd3760633677cef574150f293858e6b',
        'e3a20375afd2ee8b13181e3bbfb071094dcf70a42b50d5211013fd518ee2f4e8',
        '553a72008b772ba63d4ab95fe8ac7d8854af1c7b2788a9b258c92fee710d5113'
        ]

seed_hash = binascii.unhexlify('63eceef7919087068ac5d1b7faffa23fc90a58ad0ca89ecb224a2ef7ba282d48')

for x in range(5):
    m = "Hello RandomX {}".format(x)
    h = 1 + x
    bh = pyrx.get_rx_hash(m, seed_hash, h)
    hh = binascii.hexlify(bh).decode()
    assert hh == expected[x]

