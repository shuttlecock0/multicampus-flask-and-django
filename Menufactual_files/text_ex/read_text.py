# readlines()

# with open('mulcam.txt', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line)

# read() : 파일 내용 전체를 문자열로 return
with open('mulcam.txt', 'r') as f:
    all_text = f.read()
    print(all_text)