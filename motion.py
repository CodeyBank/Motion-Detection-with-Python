import cv2, time

# create a variable for the first frame
# None lets you create a variable and pass nothing to it so that python doesn't flag it as undefined

first_frame = None

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Introduce a Gaussian Blur into the image to remove noise(smoothing) and enhance image processing
    gray= cv2.GaussianBlur(gray, (21, 21), 0)
    # time.sleep(3)
    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)

    # set a threshold for the delta frame such that differences greater than 30 will be displayed with a white(255)
    # using the thresh binary method. for the threshold binary method, you need to access the second value of the return
    # ed tuple from the cv2.threshold method

    thresh_delta =cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow("Gray Frame", gray)
    cv2.imshow("delta frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_delta)

    key = cv2.waitKey(1)
    print(gray)
    print(delta_frame)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
