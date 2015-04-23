
def seg(input_list,seg_list):
    ret = [0] * len(seg_list)
    for row in input_list:
        for i in range(0,len(seg_list)):
            # i = [from , to]
            if(len(seg_list[i])==2):
                if(row >= seg_list[i][0] and row < seg_list[i][1]):
                    ret[i] += 1
            else:
                if(row >= seg_list[i][0]):
                    ret[i] +=1
    return ret


if __name__=='__main__':
    seg_list = [ [0,3],[3,5],[5,10] ]
    input_list = range(0,10)
    print(seg(input_list,seg_list))
