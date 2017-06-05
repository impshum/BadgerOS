import os
import cv2
import glob
import sys
import shutil
import colorful

# Image
image_path = sys.argv[1]

# Model parameters
upper_model = '/home/pi/Brain/xml/upper.xml'
hs_model = '/home/pi/Brain/xml/hs.xml'
face_model = '/home/pi/Brain/xml/face.xml'
eyes_model = '/home/pi/Brain/xml/eyes.xml'
smile_model = '/home/pi/Brain/xml/mouth.xml'

# Classifiers
clf_upper = cv2.CascadeClassifier(upper_model)
clf_hs = cv2.CascadeClassifier(hs_model)
clf_face = cv2.CascadeClassifier(face_model)
clf_eyes = cv2.CascadeClassifier(eyes_model)
clf_smile = cv2.CascadeClassifier(smile_model)

# Read the image
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect upper body
uppers = clf_upper.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=3,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)

# Detect heads
hss = clf_hs.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=10,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)

# Detect faces
faces = clf_face.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=10,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)

# Detect eyes
eyes = clf_eyes.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=10,
    minSize=(5, 5),
    flags=cv2.CASCADE_SCALE_IMAGE
)

# Detect mouths
mouths = clf_smile.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=80,
    minSize=(20, 20),
    flags=cv2.CASCADE_SCALE_IMAGE
)

# Upper box
for (x, y, w, h) in uppers:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)

# Heads box
for (x, y, w, h) in hss:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Faces box
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Eyes box
        for (x, y, w, h) in eyes:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Mouths box
            for (x, y, w, h) in mouths:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


# Begin the counting
counting = '{0}'
wooupper = counting.format(len(uppers))
woohs = counting.format(len(hss))
woofaces = counting.format(len(faces))
wooeyes = counting.format(len(eyes))
woomouths = counting.format(len(mouths))

# Results
if len(uppers) < 0:
    print 'FAILURE'
elif len(uppers) == 0:
    print colorful.bold_red('BODY:'), colorful.bold_red(wooupper)
elif len(uppers) == 1:
    print colorful.bold_green('BODY:'), colorful.bold_green(wooupper)
else:
    print colorful.bold_green('BODY:'), colorful.bold_green(wooupper)


if len(hss) < 0:
    print 'FAILURE'
elif len(hss) == 0:
    print colorful.bold_red('HEAD:'), colorful.bold_red(woohs)
elif len(hss) == 1:
    print colorful.bold_green('HEAD:'), colorful.bold_green(woohs)
else:
    print colorful.bold_green('HEAD:'), colorful.bold_green(woohs)


if len(faces) < 0:
    print 'FAILURE'
elif len(faces) == 0:
    print colorful.bold_red('FACE:'), colorful.bold_red(woofaces)
elif len(faces) == 1:
    print colorful.bold_green('FACE:'), colorful.bold_green(wooeyes)
else:
    print colorful.bold_green('FACE:'), colorful.bold_green(wooeyes)


if len(eyes) < 0:
    print 'FAILURE'
elif len(eyes) == 0:
    print colorful.bold_red('EYES:'), colorful.bold_red(wooeyes)
elif len(eyes) == 1:
    print colorful.bold_green('EYES:'), colorful.bold_green(wooeyes)
else:
    print colorful.bold_green('EYES:'), colorful.bold_green(wooeyes)


if len(mouths) < 0:
    print 'FAILURE'
elif len(mouths) == 0:
    print colorful.bold_red('GOBS:'), colorful.bold_red(woomouths)
elif len(mouths) == 1:
    print colorful.bold_green('GOBS:'), colorful.bold_green(woomouths)
else:
    print colorful.bold_green('GOBS:'), colorful.bold_green(woomouths)


countup = [int(wooupper), int(woohs), int(woofaces), int(wooeyes), int(woomouths)]
counted = sum(countup)


def binit():
    # os.remove(image_path)
    shutil.move(image_path, '/home/pi/Brain/removed/')
    print colorful.bold_red('\nFAIL - REMOVING ', os.path.basename(image_path))
    print '\n-------------\n'


def keepit():
    shutil.move(image_path, '/home/pi/Brain/gallery/')
    print colorful.bold_green('\nWINNING - KEEPING ', os.path.basename(image_path))
    print '\n-------------\n'

if counted < 0:
    binit()
elif counted == 0:
    binit()
elif counted == 1:
    binit()
elif counted == 2:
    binit()
else:
    keepit()


# Show the current image
cv2.imshow("img", image)
cv2.waitKey(1500)
cv2.destroyAllWindows()
