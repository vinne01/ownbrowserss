import qrcode as qr
nums=input("enter url")
img=qr.make(nums)
img.save("vinay.png")


