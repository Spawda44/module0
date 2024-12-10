def season(mounth):
    winter = [12, 1, 2]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    fall = [9, 10, 11]
    
    for i in winter:
        if i == int(mounth):
            print('It\'s winter!')
    for i in spring:
        if i == int(mounth):
            print('It\'s spring!')
    for i in summer:
        if i == int(mounth):
            print('It\'s summer!')
    for i in fall:
        if i == int(mounth):
            print('It\'s fall!')

def main():
    season(int(input('What month is it now? (1-12) >> ')))
    
main()