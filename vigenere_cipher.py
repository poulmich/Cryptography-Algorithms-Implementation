# Import necessary modules
import collections
import itertools
from collections import Counter

# Function to calculate the Index of Coincidence (IC)
def index_of_coincidence(text):
    """
    Calculate the Index of Coincidence (IC) for a given text.
    The IC measures how frequently pairs of identical letters appear in the text.
    Higher IC values typically indicate a simpler substitution cipher.
    """
    counts = Counter(text)
    N = len(text)
    ic = sum(value * (value - 1) for value in counts.values()) / (N * (N - 1))
    return ic

# Function to estimate key length using the Friedman test
def friedman_test(ciphertext, language_ic=0.0668):
    """
    Apply the Friedman test to estimate the key length of a Vigenère cipher.
    This function analyzes the index of coincidence for different key lengths.
    """
    max_key_length = 20  # Adjust as needed
    for key_length in range(2, max_key_length + 1):
        columns = [''.join(ciphertext[i::key_length]) for i in range(key_length)]
        ics = [index_of_coincidence(column) for column in columns]
        average_ic = sum(ics) / len(ics)
        print(f'Key Length {key_length}: IC = {average_ic:.4f}')
        if abs(average_ic - language_ic) < 0.005:  # Threshold to determine a match
            print(f'Probable key length is {key_length}')
            return key_length
    print('No probable key length found.')
    return None

# Function to decrypt Vigenère cipher using a given key
def decrypt_vigenere(ciphertext, key):
    """Decrypts the ciphertext using the Vigenère cipher with a given key."""
    key_length = len(key)
    key_as_int = [ord(i) - ord('A') for i in key]
    plaintext = ''
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            value = (ord(char) - ord('A') - key_as_int[i % key_length]) % 26
            plaintext += chr(value + ord('A'))
        else:
            plaintext += char
    return plaintext

# Function to check if a text is in English
def is_english(text, word_percentage=50, letter_percentage=85):
    """Simple heuristic to determine if a text is likely English."""
    words = text.split()
    count = len(words)
    if count == 0:
        return False
    matches = sum(1 for word in words if word.lower() in english_words)
    word_match = (float(matches) / count * 100 >= word_percentage)
    letters = [char for char in text if char.isalpha()]
    letter_match = (float(len(letters)) / len(text) * 100 >= letter_percentage)
    return word_match and letter_match

# Load a list of English words (optional, you could use nltk.corpus.words)
english_words = set(word.strip().lower() for word in open('C:\\Users\\micha\\PycharmProjects\\pythonProject2\\words_alpha.txt'))

# Constants for English letter frequency analysis
ENGLISH_FREQ_ORDER = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

# Function to decrypt Vigenère cipher using a given key
def decrypt_with_key(ciphertext, key):
    """Decrypts Vigenère cipher with a given key."""
    key_indices = [ord(k.upper()) - ord('A') for k in key]
    plaintext = []
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            offset = ord(char.upper()) - ord('A')
            decrypted_char = (offset - key_indices[i % len(key)]) % 26
            decrypted_char = chr(decrypted_char + ord('A'))
            plaintext.append(decrypted_char)
        else:
            plaintext.append(char)
    return ''.join(plaintext)

# Function to calculate chi-squared statistic
def chi_squared(column, shift):
    """Calculate the chi-squared statistic for a given shift for column data."""
    shifted = [(ord(char) - ord('A') - shift) % 26 for char in column]
    freq = collections.Counter(shifted)
    length = len(column)
    expected_freq = {ord(letter) - ord('A'): freq * length / 100 for letter, freq in zip(ENGLISH_FREQ_ORDER, [
        8.17, 14.58, 2.75, 4.25, 12.70, 2.23, 2.02, 6.09, 6.97, 0.15, 0.77, 4.03, 2.41, 6.75, 7.51,
        1.93, 0.10, 5.99, 6.33, 9.06, 2.76, 0.98, 2.36, 0.15, 1.97, 0.07])}  # Adjusted frequency for letter

    chi_sq = sum(((freq.get(k, 0) - expected_freq.get(k, 0)) ** 2) / expected_freq.get(k, 1) for k in range(26))
    return chi_sq

# Function to find the best shifts using chi-squared analysis
def find_best_shifts(column):
    """Finds the best shift for a column based on chi-squared analysis."""
    chi_scores = [(chi_squared(column, shift), shift) for shift in range(26)]
    return min(chi_scores)[1]  # Return the shift with the lowest chi-squared value

# Main function to handle Vigenère cipher decryption
def main(ciphertext, key_length):
    """Main function to handle Vigenère cipher decryption attempt."""
    ciphertext = ''.join(filter(str.isalpha, ciphertext.upper()))  # Clean and prepare ciphertext
    # Divide ciphertext into columns
    columns = [''.join(ciphertext[i::key_length]) for i in range(key_length)]
    # Determine the best shift for each column using chi-squared analysis
    shifts = [find_best_shifts(column) for column in columns]
    # Construct the decryption key from shifts
    key = ''.join(chr(shift + ord('A')) for shift in shifts)
    # Decrypt the ciphertext using the derived key
    plaintext = decrypt_with_key(ciphertext, key)
    return key, plaintext

# Example usage:
ciphertext = "MYHSIFPFGIMUCEXIPRKHFFQPRVAGIDDVKVRXECSKAPFGHMESJWUSSEHNEZIXFFLPQDVTCEUGTEEMFRQXWYCLPPAMBSKSTTPGSMIDNSESZJBDWJWSPQYINUVRFXPVPCEOZQRBNLUIINSRPXLEEHKSTTPGCEIMCSKVVVTJQRBSIUCKJOIIXXOVHYEFLINOEXFDPZJVFKTETVFXTTVJVRTBXRVGJRAIFPSRGTDXYSIWYXWVFPAQSSEHNEZIXFVRXQPRURVWBXWVCEIMCSKVVVUCXYWJAAGPUHYIDTMJFFSYUSISMIDNSESRRPILVUFSPTEIHYMEGMTVRRPREEDISHXHVTFVQKIIMFRQILVKRCAUPZTVGMCFVTIIQPRUPVEGIMWICFGIAVVRZQASJHKLQLEPUIIQSLRGGSUHSESUQQCWJCLPEWEJPRVDXGRRVHFWINCIPPLMKVYEFTLRGXSAHIJHVTBTHLGZRFDQZGVVKPRUPCSASWYSUAQWEMSUIHTPFDVHEEIVRSYITLRJVWTJXFIIWQAZVGZRYPGYWEIDNXYOKKUKIJOSYZSEEQVLMHPVTKYEXRNOEXAJVBBFAXTHXSYEEBEUSLWONRZQRPAJVTZVZQGRVGJLMGHRBUYZZMERNIFWMEYKSABYTVRRPUIVZKSAAMKHCIYDVVHYEZBETVZRQGCNSEIQSLLARRUICDCIIFWEEQCIHTVESJWITRVSUOUCHESJWMCHXSEXXTRVGJAUILFIKXTTWVELEXXXZSJPUUINWCPNTZZCCIZIEERRPXLMCZSIXDWKHYIMTVFDCEZTEERKLQGEUWFLMKISFFYSWXLGTPAHIIHFKQILVFKLQKIIMEEFJVVCWXTTWVWEZQCXZCEWOGMVGFYFUSIHYISDSUBVWEXRDSEGDXIJCLXRDVLBZZQGWRZSVAILVFYSASJFFKLQJRZHPSRJWRZCIHTRECNQKKSZQVMEGIRQYMZVQZZCMACWKVISGVLFIKXTTAFFCHYXPCWFREDJUSJTMXVZBXQQCAFAVRMCHCWKXXTGYWCHDTRMWTXUBWFTRWKHXVAKLMIQRYVWYTRKCIXGGIRBUMYEVZGFRUCRFQVRFEIFDCIFDXYCJIIWSTOELQPVDSZWMNHFBFXPTWGOZVFWIDWJIDNXYOKMECSNIGSZJWZGSYFILVDRWEXRXCWKDTIUHYINXXKSIRQHWFTDIZLLFTVEDILVKRCAULLARRBGSXFVWEILVVRXQDJDSEAUAPGOJWMCHUWTXMISIGUMQPRUHYIBDAVFKLQNXFCBJDDQKVVTQDTCSNMXAVVHLVZISKVVTQDTCSRRPHSCCEKMHQVBUMQAMSSIXKLMCZEIHTVGSIMEWWFZUMQGWUCEXSXZVMFYDHICJVWFDFIIKIEBIEKYSPTWGWJIKDYVBJPMKIPCLATDVVUZQQCXPCLVXXZVGKIXACFINLMIXFRFATPXKCKLUCORBUATPXKCWIQAAYCUVUAPPCLHUTXPCLXDTEKMFYXXOVQRXFAILGVCAJEJQRRZDRWCUHQGHFBKKUKIPCLVETPMSJXAILVGVYZCEKIIEXBIEARGTXRVAVRIXXYARGTXRVAZRPHEERDEOWMESYIMGXJMFYMGIECKQMRLZBVWKDYRFVRAIGRHKPQNSLOIIYTRPCLLMKIKVVPAKIFTYYYPRZHPMZNSLFYIMGXJMFYPDRKVRXQDRCMKLQJRCCMIPWEKSKLQJRCCMIPPRUHYIGCRRHLVMAWFZUMQGWUCEXRXKYHWSDHPRJVVKUMXVKJAGPZPVVFNMEHYIETZVBKLOWEGHVVAUWKZLOQXXZGNVUIXVBKLQZMEUUSYDJXCUMELMKVZRYPRECKSZTQRBESDPKICLTAUQVBSYFXRRZCQQCMEMFYKDYKVVTQDTCSYEHTXYSGSITVKVVTALIIHFGDTEKSDEOWMESJXTTTFKVVFDGISRXQWEGDZRQHWPCLXTTTVCGPQWEMSKLQESNSIXABEBSKLUHPZTVJDTIRBUFQPYKWWYXISDOBIFWMJZZJQPAFBUIDUYCOUZQCXLFVXTTRZBKLQCEDSFJPTQFQIEONPVHLWGHIKVRXBDAVFCIFJWRZCYZXXVZVXGHJZUYXRDVRBVAIDVCRRHQRIEHNSDAHKVRXIXPCUZZQBIEOTLMCGVHFAAGOKVRXIXPCUZZQNSLHYERJXLFVEZSSCRRKQPWVQLVUICSMKLQEVFAZWQDJKVVWQILZBXWNGYKSJLMKIIWJIZISGCNIDQYKHYIKAMVHYIKSSECKJGAJZZKLMITICDMETXYSPRQKIIKZPXSMTHRXAGWWFVIFWIDGVPHTWSIKXTTCVBJPMKIKVVTQDTCSESIAIKIJJUVLKHFJGAJZZKLMITICDMETPVHLWRXKYHKSRGIVHYIIDVCRKSPDENOPAUILEOKMACECPRVDXIIGKSPDENOPAUILXFVIPLMKVYEFTEERZRFDPVFRROTPVHLWRXKYHWSDPAFFCHAUVVOJSZPAFFCHIWIISJGUTRTSRRPEVFUIIEHAZZCPQPHKCRPXBIEGYEBEMESJWEDPUWVVEXRKVVRMBIFTUIYDGIOTCXTXLGRPXJRZHV"

keylength = friedman_test(ciphertext)
possible_keys = main(ciphertext, 7)
print("Possible Keys:", possible_keys)
for key in possible_keys:
    if is_english(key):
        print(key)
