from bip_utils import Bip39SeedGenerator, Bip84, Bip84Coins, Bip44Changes

def verify_address(mnemonic, passphrase, expected_address):
    """ Verifies that the generated Bech32 address matches the private key. """

    # Generate the seed from the mnemonic phrase
    seed = Bip39SeedGenerator(mnemonic).Generate(passphrase)

    # Create the BIP84 structure for Bitcoin (SegWit Bech32)
    bip84 = Bip84.FromSeed(seed, Bip84Coins.BITCOIN)
    bip84_acc = bip84.Purpose().Coin().Account(0)  # Account level
    bip84_chg = bip84_acc.Change(Bip44Changes.CHAIN_EXT)  # External change
    bip84_addr = bip84_chg.AddressIndex(0)  # First address

    # Retrieve the address and private key
    generated_address = bip84_addr.PublicKey().ToAddress()
    private_key_wif = bip84_addr.PrivateKey().ToWif()

    # Verify the address
    match = generated_address == expected_address

    return {
        "mnemonic": mnemonic,
        "private_key_wif": private_key_wif,
        "generated_address": generated_address,
        "expected_address": expected_address,
        "match": match
    }

# Example usage with test values
mnemonic_test = "zone custom next define truth expand version focus gentle immune dumb era kind fire tired uphold trust document pull kitchen decline clay raven menu"
passphrase_test = ""
expected_address_test = "bc1qfprx5kkkmalweumwfyeu0t8lwwntlzmp3vzp7r"  # Replace with your expected address

result = verify_address(mnemonic_test, passphrase_test, expected_address_test)

# Display results
print("📜 Mnemonic Phrase: ", result["mnemonic"])
print("🔑 Private Key (WIF): ", result["private_key_wif"])
print("🏦 Generated Address: ", result["generated_address"])
print("🎯 Expected Address: ", result["expected_address"])
print("✅ Match: ", "Yes" if result["match"] else "No")
