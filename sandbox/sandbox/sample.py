"""numpyのサンプルモジュール．
"""
import numpy as np

def stdout(obj, message):
    """標準出力する．

    Args:
        obj: 出力するオブジェクト
        message: obj出力の前に表示するメッセージ
    """
    print(message)
    print(obj)
    print()

def mult(*mats):
    """行列のリストを先頭から順に積をとって得られる行列を返す．

    Args:
        *mats: 行列のリスト

    Returns:
        行列のリストを先頭から順に積をとって得られる行列
    """
    mat = mats[0]
    for array in mats[1:]:
        mat = mat @ array

    return mat

def main():
    """サンプルを表示する．
    """
    a = np.array([[4, 1], [1, 4]])
    inv_a = np.linalg.inv(a)

    stdout(a, 'a = ')
    stdout(inv_a, 'a^{-1} = ')
    stdout(mult(a, inv_a), 'a.a^{-1} = ')
    stdout(np.linalg.eigvals(a), 'eigenvalues of a = ')

    v = np.array([[1/np.sqrt(2), 1/np.sqrt(2)], [1/np.sqrt(2), -1/np.sqrt(2)]])
    d = np.diag([5, 3])
    stdout(v, 'v = ')
    stdout(d, 'd = ')
    stdout(mult(v.T, d, v), 'v^T.d.v = ')

if __name__ == '__main__':
    main()
