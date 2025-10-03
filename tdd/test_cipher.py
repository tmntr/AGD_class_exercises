from Class_excercises.tdd.cipher import cipher
import pytest


boundary_tests = [['aaaa',-1,'zzzz'],
                  ['zzzz',1,'aaaa'],
                  ]

erroneous_shift_data = [['hello',0,'hello'],
                        ['hello',26,'hello'],
                        ['hello',52,'hello'],
                        ['hello',78,'hello'],
                        ]

funky_plaintext_data = [['HAL 9000',1,'IBM 9000'],
                        ['Hello',1,'Ifmmp'],
                        ['HELLO!',2,'JGNNQ!'],
                        ['!@£$%^&*',10,'!@£$%^&*'],
                        ['',0,'']
                        ]



stupid_user_data = [[1,2,TypeError],
                    [True,2,TypeError],
                    [1.1,2,TypeError],
                    ['A','2',TypeError],
                    ['A',True,TypeError],
                    ['A',0.1,TypeError],
                    [1,0.1,TypeError],
                    [None,2,TypeError],
                    ['Hello',None,TypeError],
                    ]
@pytest.mark.parametrize("plaintext,shift,ciphertext", erroneous_shift_data)
def test_cipher_erroneous_shifts(plaintext,shift,ciphertext):
    assert cipher(plaintext,shift) == ciphertext

@pytest.mark.parametrize("plaintext,shift,ciphertext", boundary_tests)
def test_cipher_boundaries(plaintext,shift,ciphertext):
    assert cipher(plaintext,shift) == ciphertext

@pytest.mark.parametrize("plaintext,shift,ciphertext", funky_plaintext_data)
def test_cipher_funky_plaintext(plaintext,shift,ciphertext):
    assert cipher(plaintext,shift) == ciphertext

@pytest.mark.parametrize("plaintext,shift,error_type", stupid_user_data)
def test_cipher_stupid_user(plaintext,shift,error_type):
    with pytest.raises(error_type):
        print(cipher(plaintext,shift))


