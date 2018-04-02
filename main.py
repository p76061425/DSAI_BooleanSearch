import pandas as pd

class Cache:
    def __init__(self):
        self.index_dic = {}

    def cache_op_index(self,op,index):
        if op not in self.index_dic:
            self.index_dic[op] = []
            self.index_dic[op].append(index)
        else:
            self.index_dic[op].append(index)
			

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
    source = pd.read_csv(args.source,names = ["index","title"]).values

    with open (args.query,"r",encoding = "UTF - 8") as q_f:
        queries = q_f.readlines()
        index_list = []
        
        cache = Cache()
        pre_index = cache.index_dic 
        
    # TODO compute query result
        for q_line in queries:
            query = q_line.split()
            operator = query[1]
            operands = query[::2]

            if(operator == "and"):
                and_result=[]
                in_pre_index = False
                all_in_pre_index = True
                less_index_op = operands[0]
                
                for op in operands:
                    if(op in pre_index):
                        in_pre_index = True
                        base_op = op
                    else:
                        all_in_pre_index = False

                if(all_in_pre_index):
                    and_result = pre_index[operands[0]]
                    for op in operands:
                        and_result = list(set(and_result) & set(pre_index[op]) )
                    and_result.sort()
                    and_result=[str(x) for x in and_result]
                    
                elif(in_pre_index):
                    for cached_index in pre_index[base_op]:
                        for op in operands:
                            find_and = True
                            find = source[cached_index-1][1].find(op)
                            if(find<0):
                                find_and = False
                                break
                        if(find_and):
                            and_result.append(str(cached_index))
                else:
                    for title in source:
                        find_and = True
                        for op in operands:
                            find = title[1].find(op)
                            if(find>=0):
                                cache.cache_op_index(op,title[0])
                            else:
                                find_and = False
                        if(find_and):
                            and_result.append(str(title[0]) )
                    
                if(len(and_result)==0):
                    and_result.append("0")
                
                and_result_str = ','.join(and_result)
                index_list.append(and_result_str)
                
            elif(operator == "or"):
                or_result = []
                in_cache_op = []
                out_op = []
                for op in operands:
                    if op in pre_index:
                        in_cache_op.append(op)
                    else:
                        out_op.append(op)
                for op in out_op:
                    for title in source:
                        find = title[1].find(op)
                        if(find>=0):
                            or_result.append(title[0])
                            cache.cache_op_index(op,title[0])
                or_result = list(set(or_result))
                
                for op in in_cache_op:
                    or_result = list( set(or_result) | set(pre_index[op]) )

                if(len(or_result)==0):
                    or_result.append(0)  
                
                or_result.sort()
                or_result=[str(x) for x in or_result]
                or_result_str = ','.join(or_result)
                index_list.append(or_result_str)

            elif(operator == "not"):
                not_result = []
                if(operands[0] in pre_index):
                    not_result = pre_index[operands[0]]
                    for not_op in operands[1:]:
                        if(not_op in pre_index):
                            not_result = list(set(not_result) - set(pre_index[not_op]))
                        else:
                            not_list = []
                            for base_index in pre_index[operands[0]]:
                                find = source[base_index-1][1].find(not_op)
                                if(find>=0):
                                    not_list.append(base_index)
                            not_result = list(set(not_result) - set(not_list) )
                else:
                    not_result = [ ]
                    for title in source:
                        find_not = False
                        find_first = title[1].find(operands[0])
                        if(find_first>=0):
                            cache.cache_op_index(operands[0],title[0])
                            for n_op in operands[1:]:
                                find_n_op = title[1].find(n_op)
                                if(find_n_op>=0):
                                    find_not = True
                                    break 
                            if(find_not==False):
                                not_result.append( title[0] )
                        
                    if(len(not_result)==0):
                        not_result.append(0)           
                
                if(operands[0] in pre_index):
                    not_result.sort()
                not_result=[str(x) for x in not_result]
                not_result_str = ','.join(not_result)
                index_list.append(not_result_str)

        index_list_str = "\n".join(index_list)
                
    # TODO output result
        with open(args.output, 'w') as output_file:
            output_file.write(index_list_str)
            			