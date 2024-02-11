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
# それぞれの状態遷移をカウントする
  M = [0,0,0,0]

  for i in range(len(image) - 1):
    if image[i] == '0' and image[i+1] == '0':
        M[0] += 1
    elif image[i] == '1' and image[i+1] == '0':
        M[1] += 1
    elif image[i] == '0' and image[i+1] == '1':
        M[2] += 1
    else :
        M[3] += 1
# 定常確率の計算
  Ps = [0.0, 0.0]
  Ps[0] = M0 / (M0 + M1)
  Ps[1] = M1 / (M0 + M1)
  print(f'Ps0 = {Ps[0]}, Ps1 = {Ps[1]}')

#条件付確率の計算
  Pc = [0.0,0.0,0.0,0.0]
#0→0
  Pc[0] = M[0] / (M[0] + M[1])
#0→1
  Pc[1] = M[1] / (M[0] + M[1])
#1→0
  Pc[2] = M[2] / (M[2] + M[3])
#1→1
  Pc[3] = M[3] / (M[2] + M[3])

  print(f'P(0|s0) = {Pc[0]}, P(1|s0)= {Pc[2]},P(0|s1) = {Pc[1]}, P(1|s1) = {Pc[3]}')
#条件付エントロピーの計算
  Hs = [0.0,0.0]
  Hs[0] += -Pc[0]*math.log2(Pc[0])
  Hs[0] += -Pc[1]*math.log2(Pc[1])
  Hs[1] += -Pc[2]*math.log2(Pc[2])
  Hs[1] += -Pc[3]*math.log2(Pc[3])
 
  H = 0
  for i in range(len(Ps)):
    H += Ps[i] * Hs[i]

  print(f'H = {H}')

if __name__ == "__main__":
  main()