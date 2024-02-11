import math

def read_file(path):
  """
  画像ファイルを読み込む関数

  Parameters
  ----------
  path : str
    画像ファイルのパス
 
  Returns
  ----------
  image : str
    0 / 1 で表現される画像列．演習では 128 x 128 の大きさであるため長さは 16384
  """
  with open(path) as f:
    s = f.read()
  return s

def main():

  # 読み込む image の名前(パス)
  name = "image2"
  image = read_file(name)

  M0 = image.count('0')
  M1 = image.count('1')
  P = [0.0, 0.0]
  P[0] = M0 / (M0 + M1)
  P[1] = M1 / (M0 + M1)
  print(f'P0 = {P[0]}, P1 = {P[1]}')

  # math.log2(0) が　-∞ となってしまうのを防ぐ
  for i in range(len(P)):
    if P[i] == 0:
      P[i] = 1
 
  H = 0
  for p in P:
    H += -p*math.log2(p)

  print(f'H = {H}')

if __name__ == "__main__":
  main()