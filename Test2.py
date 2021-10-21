import pydicom

dcom445 = pydicom.dcmread("D:\\test_data\\6305199666339888\\CBCT\\I3857")
print(dcom445.ImagePositionPatient)
dcom446 = pydicom.dcmread("D:\\test_data\\6305199666339888\\CBCT\\I3858")
print(dcom446.ImagePositionPatient)
dcom447 = pydicom.dcmread("D:\\test_data\\6305199666339888\\CBCT\\I3859")
print(dcom447.ImagePositionPatient)

dcom0 = pydicom.dcmread("D:\\test_data\\6305199666339888\\CT\\0.dcm")
dcom1 = pydicom.dcmread("D:\\test_data\\6305199666339888\\CT\\1.dcm")
dcom2 = pydicom.dcmread("D:\\test_data\\6305199666339888\\CT\\2.dcm")
print(dcom0.ImagePositionPatient)
print(dcom1.ImagePositionPatient)
print(dcom2.ImagePositionPatient)


dcom3 = pydicom.dcmread("D:\\test_data\\6305199666339888\\SCT\\0.dcm")
dcom4 = pydicom.dcmread("D:\\test_data\\6305199666339888\\SCT\\1.dcm")
dcom5 = pydicom.dcmread("D:\\test_data\\6305199666339888\\SCT\\2.dcm")
print(dcom3.ImagePositionPatient)
print(dcom4.ImagePositionPatient)
print(dcom5.ImagePositionPatient)
'''
pixel=dcom3.pixel_array
for i in range(0,511):
    for j in range(0,511):
        print(str(pixel[i][j])+" ",end='')
    print()
'''
