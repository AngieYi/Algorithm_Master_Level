
def lis(a):
    opt = []
    tmp = []
    i = 0
    count = 1
    opt.append((1,[a[0]]))

    while (i < len(a)-1):
        while(a[i] < a[i+1] and (i < len(a)-1)):
            count += 1
            tmp.append(a[i])
            tmp.append(a[i+1])
            # print max(opt)
            # print max(opt)[0]
            # print max(opt)[1]

            if a[i+1] > max(opt)[1][-1]:
                tmplist = list(max(opt)[1])
                tmplist.append(a[i+1])
                opt.append((max(opt)[0]+1,tmplist))
            elif(count >= max(opt)[0]):
                opt.append((count,tmp))
            count = 1
            tmp = []
            i += 1
        i += 1
    return max(opt)[1]

if __name__ == '__main__':
    print lis("aebbcg")


