import numpy as np
import cv2
import jiro_sound
import graph

# 任意のx座標中の白をカウントする
def calcVal(img, x):
    val = 0
    for i in img[:, x]:
        if i == 255:
            val+=1
    return val

# 全画素中の白をカウントする
def calcAllVal(img):
    return cv2.countNonZero(img)

# 任意のx座標での列を返却する
def getColumn(img, x):
    return img[:, x]

def calcVal2(arr1, arr2):
    return np.sum(abs((arr1-arr2)/255))

# ここからメインの処理

# 音周りの初期化
jiroSound = jiro_sound.JiroSound()

# グラフ周りの初期化
graph = graph.Graph()

print('initialize camera')
cap = cv2.VideoCapture(1)
fgbg = cv2.createBackgroundSubtractorMOG2()

# オープニング処理
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

# 物体が通過したかの値を管理
vals = np.zeros((2, 960))
val = np.zeros(960)
val_pre = np.zeros(960)
loop = 0

print('main process start')

while(1):
    # 動画を1フレーム読み込む
    ret, frame = cap.read()

    # 「Escが押される」または「動画フレームがない場合」終了
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
    # 動体、背景、影に分ける
    fgmask = fgbg.apply(frame)
    
    # 二値化
    _, fgmask = cv2.threshold(fgmask,127,255,cv2.THRESH_BINARY)
    # オープニング処理
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    # 表示
    cv2.imshow('frame',fgmask)

    # 通過数をカウント
    height, width = fgmask.shape[:2]
    pixels = width * height
    val = getColumn(fgmask, int(width/2)) # 中央
    #vals[0][loop] = getColumn(fgmask, int(width/2)) # 中央
    #vals[1][loop] = getColumn(fgmask, int(width/4)) # 左半分
    #vals[2][loop] = getColumn(fgmask, int(width/4*3)) # 右半分
    #result = calcVal2(vals[0][0], vals[0][1]) + calcVal2(vals[1][0], vals[1][1]) +calcVal2(vals[2][0], vals[2][1])
    result = calcVal2(val, val_pre)
    # 評価値として正規化
    #print(str(result) + " " + str(val) + " " + str(val_pre))
    print(str(result))
    # 音を鳴らす
    jiroSound.play_sound(result, vals.size*height)
    # グラフを描画
    graph.drawing(result)

    #print("loop: " + str(loop))
    #loop = (loop+1)%vals.size
    val_pre = val
            
cap.release()
cv2.destroyAllWindows()
