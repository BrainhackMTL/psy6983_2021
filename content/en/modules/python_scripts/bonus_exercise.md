In this exercise we will code a key-based encryption and decryption system. The principle is similar to the [Vignere cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher), but instead of just using the keys to just to shift the letters, we will be using a slightly more complex transformation.

The Vignere cipher consists in shifting the letters of the message to encrypt by the index of the corresponding letter in the key. For example the encryption of the letter B with the key D will result of the letter of index = index(B) + index(D) = 2 + 4 = 6, so it will be F.

:warning: Note that here by index I mean the index of the letter in the alphabet (or in the character table you use) and not the index of the letter in the message string.


You pair up the letters of the message with the ones of the key one by one, and repeating the key if it is shorter than the message. For example if the message is `My awesome message` and the key is `my key`, the pairs will be :
```
(M,m),
(y,y),
(a,k),
(w,e),
(e,y),
(s,m),
(o,y),
(m,k) ...
```
and so on.

Here we will follow this principle, but instead of directly having `index(message_letter) + index(key_letter)` as the index of the encrypted letter, we will turn it into an other base, depending on the rest of the division of the key's index by 5. So the base `k` of the encrypted letter will be : `k = 5 + (index(key_letter) % 5)`.
For example if the index of the message letter is 47 and the index of the key letter is 19, the index of the encrypted letter will be 47 + 19 = 66, which should be turned into base 5 + 4 = 9 which finally gives 73 (indeed 7*9 + 3 = 66).

For the indices of the letter, we will not use the the number of the letter in the alphabet, but the unicode index of the letter, which is easily obtained with the native python function `ord`. The reverse operation of getting a letter from its unicode index is obtained with native python function `chr`. There are 1114112 unicode characters handled by python, so we'll have to make sure we have indices in the range 0 to 1114111. To ensure that, we can use values modulo 1114112, i.e. `encrypted_index = base_k(ord(message_letter) + ord(key_letter), k) % 1114112`.

In a file `cipher.py`, you'll implement the following functions :
* `base_k(n, k)` : return the number `n` in the base of `k`. E.g. `base_k(78, 7)` should return `141`.
* `base_10(n, k)` : return in base 10 the number `n` considered in base `k`, e.g. `base_10(141, 7)` should return `78`.
* `encrypt_letter(letter, key)` : return the encrypted letter with the key, e.g. `encrypt_letter("l", "k")` should return `'Ʃ'`.
* `decrypt_letter(letter, key)` : return the decrypted letter with the key, e.g. `decrypt_letter("Ʃ", "k")` should return `'l'`.
* `process_message(message, key, encrypt)`: return the encrypted message using the letters in `key` if encrypt is `True`, and the decrypted message if encrypt is `False`. For example :
```
process_message('coucou', 'clef', True)
'ðōϪƕýŕ'

process_message('ðōϪƕýŕ', 'clef', False)
'coucou'
```

Then complete the script so that you can call your script with arguments as follows :
```
python cipher.py --message "coucou" --key "clef" --mode enc
'ðōϪƕýŕ'

python cipher.py --message "ðōϪƕýŕ" --key "clef" --mode dec
'coucou'
```

Finally, decrypt the following text :
```
Ô÷ԼВzϾ֍ćЁ¡ȦóІԩţϭĭВƐÉÉչȧôđȒЀĮƩȒЉƛìāԼњyչչĮƔöȖĬЇՀϽϩyԪţƝćքϩöČȖƔóƮȕƝţāԨԬúϾӅÒǾ¡ƧyЊչϷϼĬѷƦàąԳȕöþƓϫþưȝВèßĂԬѢąԟԲþȩ±ȖĄѡѡȠϼþԽƮëÈӈȝýöƛƳĶȜ϶ƦäĎэԵþԠ
```
with the following key :
```
This is the (not so) secret key.
```

### Bonus in the bonus (bonusception)

Modify your script so that the message and key arguments can be paths to text files. To do this I suggest you use the `isfile` function from the `os.path` package :
```
import os

os.path.isfile(mystring)
```
It will return True if mystring is a valid path to a file and False otherwise.

Then if your script detects arguments that are paths to files, it should use the text contained in the file.
Also, if the message argument is a path to a file, the processed message should be saved to a new file with the same name appended with "_encrypted" or "_decrypted" depending on the mode argument.

After that you can use the decrypted text from earlier as a key to decrypt the file obtained with :
```
wget https://raw.githubusercontent.com/BrainhackMTL/psy6983_2021/master/content/en/modules/python_scripts/message_encrypted.txt
```
