from demo.models import FACTORY_PRICE,ASSET_PRICE,WEIGHT,ASSET_TYPE,ASSET_VARITY,FACTORY_TYPE,COMMON_INFORMATION,BOND


# 2011-4-18

#调整期货比例

class M6(object):

    def inital(templist,type):

        inital_list=[]

        for item in templist:
            inital_list.append(item.cap)

        # 初始化s与result_List
        s = set(inital_list)
        result_List = []

        # result_List为templist去重、升序的结果
        for item in s:
            result_List.append(item)
        if type=='reverse':
            result_List.sort(reverse=True) #大到小排序
        else:
            result_List.sort(reverse=False)
        return result_List


    def adjust(fare,templist):

        result_List = M6.inital(templist,'not_reverse') #小到大排序

        type_id=templist[0].asset_type_id

        # 金额为0时，动态调整结束
        while(fare>0):

            if len(result_List)>1:
                count=0
                first_small=result_List[0]
                second_small=result_List[1]

                # 统计最小项数目
                for item in templist:
                    if item.cap==first_small:
                        count+=1

                if (second_small-first_small)*count>fare:

                    # 修改ASSET_VARITY对应项
                    for index in range(len(templist)):
                        if templist[index].cap==first_small:
                            item_varity_cap=templist[index].cap+fare/count
                            ASSET_VARITY.objects.filter(id=templist[index].id).update(cap=item_varity_cap)

                    # 金额置0
                    fare=0  #fare已经全部用掉了

                else:

                    # 修改ASSET_VARITY对应项
                    for index in range(len(templist)):
                        if templist[index].cap==first_small:
                            item_varity_cap =second_small
                            ASSET_VARITY.objects.filter(id=templist[index].id).update(cap=item_varity_cap)

                    # 金额削减
                    fare-=(second_small-first_small)*count

                    # 重置list
                    templist = ASSET_VARITY.objects.filter(asset_type_id=type_id)

                    # 重置result_List
                    result_List=M6.inital(templist,'not_reverse')
                    
            #当四个值相等时
            else:
                captemp=fare/4
                idtemp=[2,3,4,5]
                for i in idtemp:
                    futures_temp_cap=ASSET_VARITY.objects.get(id=i).cap
                    futures_temp_cap=futures_temp_cap+captemp
                    ASSET_VARITY.objects.filter(id=i).update(cap=futures_temp_cap)
                fare=0



    def adjust_reverse(fare,templist):

        result_List = M6.inital(templist,'reverse')

        type_id = templist[0].asset_type_id

        # 金额为0时，动态调整结束
        while (fare > 0):
            if len(result_List)>1:
                count = 0
                first_big = result_List[0]
                second_big = result_List[1]

                # 统计最大项数目
                for item in templist:
                    if item.cap == first_big:
                        count += 1

                if (first_big - second_big) * count > fare:

                    # 修改ASSET_VARITY对应项
                    for index in range(len(templist)):
                        if templist[index].cap== first_big:
                            item_varity_cap = templist[index].cap - fare / count
                            ASSET_VARITY.objects.filter(id=templist[index].id).update(cap=item_varity_cap)


                    # 金额置0
                    fare = 0
                else:

                    # 修改ASSET_VARITY对应项
                    for index in range(len(templist)):
                        if templist[index].cap == first_big:
                            item_varity_cap = second_big
                            ASSET_VARITY.objects.filter(id=templist[index].id).update(cap=item_varity_cap)

                    # 金额削减
                    fare -= (first_big - second_big) * count

                    # 重置list
                    templist = ASSET_VARITY.objects.filter(asset_type_id=type_id)

                    # 重置result_List
                    result_List = M6.inital(templist,'reverse')
            else:
                captemp=fare/4
                idtemp=[2,3,4,5]
                for i in idtemp:
                    futures_temp_cap=ASSET_VARITY.objects.get(id=i).cap
                    futures_temp_cap=futures_temp_cap-captemp
                    ASSET_VARITY.objects.filter(id=i).update(cap=futures_temp_cap)
                fare=0


