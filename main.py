import os
import cv2

from option import args
import salt_and_pepper
import gaussian

src = []
dst = []
dst_path = None
if os.path.isfile(args.src):
    if args.dst is None:
        dst_path = os.path.join(os.path.dirname(args.src), 'results')
        dst.append(os.path.join(dst_path, os.path.basename(args.src)))
    else:
        dst_path = os.path.dirname(args.dst)
        dst.append(args.dst)
    image = cv2.imread(args.src)
    if image is not None:
        src.append(image)
        print(args.src)
elif os.path.isdir(args.src):
    if args.dst is None:
        dst_path = os.path.join(args.src, 'results')
    else:
        dst_path = args.dst

    files = os.listdir(args.src)
    for file in files:
        name = os.path.join(args.src, file)
        image = cv2.imread(name)
        if image is not None:
            src.append(image)
            print(name)
            dst.append(os.path.join(dst_path, file))
else:
    print('src error. :', args.src)

print(dst_path)

if dst_path and not os.path.isdir(dst_path):
    os.mkdir(dst_path)

for i, image in enumerate(src):
    result = None
    if args.method == 'salt_and_pepper':
        result = salt_and_pepper.generate_salt_and_pepper_noise(image, args.p)
    elif args.method == 'gaussian':
        result = gaussian.generate_gaussian_noise(image, args.var)
    else:
        print('method error. :', args.method)
    cv2.imwrite(dst[i], result)
    print(dst[i])