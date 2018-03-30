import pandas as pd

if __name__ == '__main__':
    # You should not modify this part.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--source',
                       default='source.csv',
                       help='input source data file name')
    parser.add_argument('--query',
                        default='query.txt',
                        help='query file name')
    parser.add_argument('--output',
                        default='output.txt',
                        help='output file name')
    parser.add_argument('-f',
                        default=None,
                        help='')
    
    args = parser.parse_args()
    
    # Please implement your algorithm below
    
    # TODO load source data, build search engine

    # TODO compute query result
  
    # TODO output result
    
    source = pd.read_csv(args.source,names = ["title"])
    query = pd.read_csv(args.query,header = None)

#     print(source)
#     print(query)
    
    with open(args.output, 'w') as output_file:
        a = 87
    
    for row in range(query.shape[0]):
        query_list = []
        print(query[0][row])
        and_pos = -1
        or_pos = -1
        not_pos =-1
        and_pos = query[0][row].find(" and ")
        or_pos = query[0][row].find(" or ")
        not_pos = query[0][row].find(" not ")

        if(and_pos>=0):
            query_list = query[0][row].split(" and ")
            print("operation:", "and")
        elif(or_pos>=0):
            query_list = query[0][row].split(" or ")
            print("operation:","or")
        elif(not_pos>=0):
            query_list = query[0][row].split(" not ")
            print("operation:","not")

        print("query_list",query_list)
        print("and_pos",and_pos)
        print("or_pos",or_pos)
        print("not_pos",not_pos)
        
        
        print("-------------------------搜尋結果--------------------------------")    
        
        index_list = []        

        for i in range(source.shape[0]):

            if(and_pos>=0):
                find_num = 0
                for sub_str in range (len(query_list)):                    
                    find = source["title"][i+1].find(query_list[sub_str])
                    if(find>=0):
                        find_num+=1
                        
                if(find_num == len(query_list)):
                    print("index:",i+1,"find:",find,source["title"][i+1])
                    index_list.append(i+1)
#                     print("index_lsit",index_list)
#                     index_list_str = str(index_list).strip('[,\',]')
#                     print(index_list_str) 
 
            elif(or_pos>=0):
                find_num = 0
                for sub_str in range (len(query_list)):
                    if(find_num == 0):
                        find = source["title"][i+1].find(query_list[sub_str])
                        if(find>=0):
                            find_num+=1
                if(find_num > 0):
                    print("index:",i+1,"find:",find,source["title"][i+1])
                    index_list.append(i+1)
#                     print("index_lsit",index_list)
#                     index_list_str = str(index_list).strip('[,\',]')
#                     print(index_list_str)
 
            elif(not_pos>=0):
                find_not = 0
                find = source["title"][i+1].find(query_list[0])
                if(find>=0):
                    for sub_str in range (len(query_list)-1):
                       if(find_not == 0):
                           find = source["title"][i+1].find(query_list[sub_str+1])
                           if(find>=0):
                               find_not+=1
                    if(find_not == 0):
                        print("index:",i+1,"find_not:",find_not,source["title"][i+1])              
                        index_list.append(i+1)
#                         print("index_lsit",index_list)
#                         index_list_str = str(index_list).strip('[,\',]')
#                         print(index_list_str)

        print("------------------------index_list_str-------------------------")
#         if(len(index_list)==0):
#             with open(args.output, 'a') as output_file:
#                 output_file.write("0"+'\n')
#         else:
#             index_list_str = str(index_list).strip('[,\',]')
#             index_list_str = index_list_str.strip()
#             print(index_list_str)
#             with open(args.output, 'a') as output_file:
#                 output_file.write(index_list_str+'\n')
        
        if(len(index_list)!=0):
            n1_index = index_list[0]
            with open(args.output, 'a') as output_file:
                output_file.write(str(index_list[0]))
                for i in range(len(index_list)-1):
                    output_file.write(','+str(index_list[i+1]))
                output_file.write('\n')
            print(index_list)
        else:
            with open(args.output, 'a') as output_file:
                output_file.write('0'+'\n')
            print(index_list)
        print("---------------------------------------------------------------")