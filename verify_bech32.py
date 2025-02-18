from bip_utils import Bip39SeedGenerator, Bip84, Bip84Coins, Bip44Changes

def verify_address(mnemonic, passphrase, expected_address):
    """ Vérifie que l'adresse Bech32 générée correspond à la clé privée. """

    # Génération de la seed depuis la phrase mnémonique
    seed = Bip39SeedGenerator(mnemonic).Generate(passphrase)

    # Création de la structure BIP84 pour Bitcoin (SegWit Bech32)
    bip84 = Bip84.FromSeed(seed, Bip84Coins.BITCOIN)
    bip84_acc = bip84.Purpose().Coin().Account(0)  # Niveau compte
    bip84_chg = bip84_acc.Change(Bip44Changes.CHAIN_EXT)  # Change 0 (externe)
    bip84_addr = bip84_chg.AddressIndex(0)  # Première adresse

    # Récupération de l'adresse et de la clé privée
    generated_address = bip84_addr.PublicKey().ToAddress()
    private_key_wif = bip84_addr.PrivateKey().ToWif()

    # Vérification de l'adresse
    match = generated_address == expected_address

    return {
        "mnemonic": mnemonic,
        "private_key_wif": private_key_wif,
        "generated_address": generated_address,
        "expected_address": expected_address,
        "match": match
    }

# Exemple d'utilisation avec des valeurs test
mnemonic_test = "zone custom next define truth expand version focus gentle immune dumb era kind fire tired uphold trust document pull kitchen decline clay raven menu"
passphrase_test = ""
expected_address_test = "bc1qfprx5kkkmalweumwfyeu0t8lwwntlzmp3vzp7r"  # Remplace avec l'adresse obtenue

result = verify_address(mnemonic_test, passphrase_test, expected_address_test)

# Affichage des résultats
print("📜 Phrase Mnémonique : ", result["mnemonic"])
print("🔑 Clé Privée (WIF) : ", result["private_key_wif"])
print("🏦 Adresse Générée : ", result["generated_address"])
print("🎯 Adresse Attendue : ", result["expected_address"])
print("✅ Correspondance : ", "Oui" if result["match"] else "Non")
