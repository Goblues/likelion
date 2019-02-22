from faker import Faker

myfake = Faker()

# Faker의 메소드를 통해 어떤 종류의 가짜데이터를 뽑아낼지 결정 가능
# Seed 파일 코드를 실행할 때마다 같은 faker 결과를 도출해주는 파일
myfake.seed(1)

print(myfake.name())
print(myfake.address())
print(myfake.text())
print(myfake.state())
print(myfake.sentence())
print(myfake.random_number())
