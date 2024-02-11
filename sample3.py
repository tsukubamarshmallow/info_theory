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
# 00,01,10,11の存在数をカウント
  M = [0,0,0,0]

  for i in range(len(image) - 1):
    if image[i] == '0' and image[i+1] == '0':
        M[0] += 1
    elif image[i] == '0' and image[i+1] == '1':
        M[1] += 1
    elif image[i] == '1' and image[i+1] == '0':
        M[2] += 1
    else :
        M[3] += 1
# 00→0,00→1,01→0,01→1...の回数をそれぞれカウント
  MM = [0,0,0,0,0,0,0,0]
  for i in range(len(image) - 2):
    if image[i] == '0' and image[i+1] == '0' and image[i+2] == '0':
        MM[0] += 1
    elif image[i] == '0' and image[i+1] == '0' and image[i+2] == '1':
        MM[1] += 1
    elif image[i] == '0' and image[i+1] == '1' and image[i+2] == '0':
        MM[2] += 1
    elif  image[i] == '0' and image[i+1] == '1' and image[i+2] == '1':
        MM[3] += 1
    elif image[i] == '1' and image[i+1] == '0' and image[i+2] == '0':
        MM[4] += 1
    elif  image[i] == '1' and image[i+1] == '0' and image[i+2] == '1':
        MM[5] += 1
    elif image[i] == '1' and image[i+1] == '1' and image[i+2] == '0':
        MM[6] += 1
    elif  image[i] == '1' and image[i+1] == '1' and image[i+2] == '1':
        MM[7] += 1
# 定常確率の計算
  Ps = [0.0, 0.0,0.0,0.0]
  Ps[0] = M[0] / (M[0] + M[1] + M[2] + M[3])
  Ps[1] = M[1] / (M[0] + M[1] + M[2] + M[3])
  Ps[2] = M[2] / (M[0] + M[1] + M[2] + M[3])
  Ps[3] = M[3] / (M[0] + M[1] + M[2] + M[3])
  print(f'Ps0 = {Ps[0]}, Ps1 = {Ps[1]},Ps2 = {Ps[2]}, Ps3 = {Ps[3]}')

#条件付確率の計算
  Pc = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
#00→0
  Pc[0] = MM[0] / (MM[0] + MM[1])
#00→1
  Pc[1] = MM[1] / (MM[0] + MM[1])
#01→0
  Pc[2] = MM[2] / (MM[2] + MM[3])
#01→1
  Pc[3] = MM[3] / (MM[2] + MM[3])
#10→0
  Pc[4] = MM[4] / (MM[4] + MM[5])
#10→1
  Pc[5] = MM[5] / (MM[4] + MM[5])
#11→0
  Pc[6] = MM[6] / (MM[6] + MM[7])
#11→1
  Pc[7] = MM[7] / (MM[6] + MM[7])

  print(f'P(0|s0) = {Pc[0]}, P(0|s1) = {Pc[2]},P(0|s2) = {Pc[4]}, P(0|s3) = {Pc[6]},P(1|s0) = {Pc[1]}, P(1|s1) = {Pc[3]},P(1|s2) = {Pc[5]}, P(1|s3) = {Pc[7]}')
#条件付エントロピーの計算
  Hs = [0.0,0.0,0.0,0.0]
  Hs[0] += -Pc[0]*math.log2(Pc[0])
  Hs[0] += -Pc[1]*math.log2(Pc[1])
  Hs[1] += -Pc[2]*math.log2(Pc[2])
  Hs[1] += -Pc[3]*math.log2(Pc[3])
  Hs[2] += -Pc[4]*math.log2(Pc[4])
  Hs[2] += -Pc[5]*math.log2(Pc[5])
  Hs[3] += -Pc[6]*math.log2(Pc[6])
  Hs[3] += -Pc[7]*math.log2(Pc[7])
 
  H = 0
  for i in range(len(Ps)):
    H += Ps[i] * Hs[i]

  print(f'H = {H}')

if __name__ == "__main__":
  main()