from demo.models import FACTORY_PRICE,ASSET_PRICE,WEIGHT,ASSET_TYPE,ASSET_VARITY,FACTORY_TYPE,COMMON_INFORMATION,BOND


# 2011-4-18

class M6(object):

    def inital(list,type):

        inital_list=[]

        for item in list:
            inital_list.append(item.cap)

        # 初始化s与result_List
        s = set(inital_list)
        result_List = []

        # result_List为list去重、升序的结果
        for item in s:
            result_List.append(item)
        if type=='reverse':
            result_List.sort(reverse=True)
        else:
            result_List.sort(reverse=False)
        return result_List


    def adjust(fare,list):

        result_List = M6.inital(list,'not_reverse')

        type_id=list[0].asset_type_id

        # 金额为0时，动态调整结束
        while(fare>0and len(result_List)>1):

            count=0
            first_small=result_List[0]
            second_small=result_List[1]

            # 统计最小项数目
            for item in list:
                if item.cap==first_small:
                    count+=1

            if (second_small-first_small)*count>fare:

                # 修改ASSET_VARITY对应项
                for index in range(len(list)):
                    if list[index].cap==first_small:
                        item_varity_cap=list[index].cap+fare/count
                        ASSET_VARITY.objects.filter(id=list[index].id).update(cap=item_varity_cap)

                # 金额置0
                fare=0

            else:

                # 修改ASSET_VARITY对应项
                for index in range(len(list)):
                    if list[index].cap==first_small:
                        item_varity_cap =second_small
                        ASSET_VARITY.objects.filter(id=list[index].id).update(cap=item_varity_cap)

                # 金额削减
                fare-=(second_small-first_small)*count

                # 重置list
                list = ASSET_VARITY.objects.filter(asset_type_id=type_id)

                # 重置result_List
                result_List=M6.inital(list,'not_reverse')


    def adjust_reverse(fare,list):

        result_List = M6.inital(list,'reverse')

        type_id = list[0].asset_type_id

        # 金额为0时，动态调整结束
        while (fare > 0 and len(result_List)>1):

            count = 0
            first_big = result_List[0]
            second_big = result_List[1]

            # 统计最大项数目
            for item in list:
                if item.cap == first_big:
                    count += 1

            if (first_big - second_big) * count > fare:

                # 修改ASSET_VARITY对应项
                for index in range(len(list)):
                    if list[index].cap== first_big:
                        item_varity_cap = list[index].cap - fare / count
                        ASSET_VARITY.objects.filter(id=list[index].id).update(cap=item_varity_cap)


                # 金额置0
                fare = 0
            else:

                # 修改ASSET_VARITY对应项
                for index in range(len(list)):
                    if list[index].cap == first_big:
                        item_varity_cap = second_big
                        ASSET_VARITY.objects.filter(id=list[index].id).update(cap=item_varity_cap)

                # 金额削减
                fare -= (first_big - second_big) * count

                # 重置list
                list = ASSET_VARITY.objects.filter(asset_type_id=type_id)

                # 重置result_List
                result_List = M6.inital(list,'reverse')


