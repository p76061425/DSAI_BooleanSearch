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
    
    source = pd.read_csv(args.source,names = ["index","title"]).values

    with open (args.query,"r",encoding = "UTF - 8") as q_f:
        queries = q_f.readlines()
        index_list = []
    
        for q_line in queries:
            query = q_line.split()
            operator = query[1]
            operands = query[::2]

#             print(operator)
#             print(operands)

            if(operator == "and"):
                and_result=[]
                #搜尋source
                for title in source:
                    find_and = True
                    #搜尋title的每個operand
                    for op in operands:
                        find = title[1].find(op)
                        if(find==-1):
                            find_and = False
                            break
                    if(find_and):
                        and_result.append( str(title[0]) )

                if(len(and_result)==0):
                    and_result.append("0")
                
                and_result_str = ','.join(and_result)
                index_list.append(and_result_str)
            
            
            elif(operator == "or"):
                or_result = []
                for title in source:
                    find_or = False
                    for op in operands:
                        find = title[1].find(op)
                        if(find>=0):
                            find_or = True
                            break
                    if(find_or):
                        or_result.append( str(title[0]) )

                if(len(or_result)==0):
                    or_result.append("0")  
                    
                or_result_str = ','.join(or_result)
                index_list.append(or_result_str)

                
            elif(operator == "not"):
                not_result = []
                for title in source:
                    find_not = False
                    find_first = title[1].find(operands[0])
                    if(find_first>=0):
                        for i in range(len(operands)-1):
                            find_n_op = title[1].find(operands[i+1])
                            if(find_n_op>=0):
                                find_not = True
                                break
                        if(find_not==False):
                            not_result.append( str(title[0]) )

                if(len(not_result)==0):
                    not_result.append("0")           
                    
                not_result_str = ",".join(not_result) 
                index_list.append(not_result_str)

#             print("="*80)
            
        index_list_str = "\n".join(index_list)
        
        with open(args.output, 'w') as output_file:
            output_file.write(index_list_str)
            
            