import numpy as np
import cv2

# 任意のx座標中の白をカウントする
def calcVal(img, x):
    val = 0
    for i in img[:, x]:
        if i == 255:
            val+=1
    return val

# ここからメインの処理
cap = cv2.VideoCapture(1)
fgbg = cv2.createBackgroundSubtractorMOG2()

# オープニング処理
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

# 物体が通過したかの値を管理
vals = np.zeros(10)
loop = 0

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

    # 中央の通過数をカウント
    height, width = fgmask.shape[:2]
    vals[loop] = calcVal(fgmask, int(width/2))
    result = np.sum(vals)
    # 評価値として正規化
    print(str(int(result/(height*len(vals))*100)) + " " + str(vals))

    loop = (loop+1)%10
            
cap.release()
cv2.destroyAllWindows()
