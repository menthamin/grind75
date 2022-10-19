"""3Sum
- https://leetcode.com/problems/3sum/
    1. 1개 값을 고정 후 [목표값 - 고정값]으로 목표값 을 변경한다.

    2. 고정값 이후 num으로 2Sum 로직 실행
    3. 고정값 이후 첫번째 값을 hashmap에 넣는다.
    4. 다음 값(2차 고정값)부터 차례대로 for문을 돌며 [변경된 고정값 - 현재값] 이 hashmap에 있는지 확인한다.
        4.1. hashmap에 있으면 (1차 고정값, 2차 고정값, hashmap값) 을 정렬 후 결과 집합에 넣는다.
        4.2. 없으면 2차 고정값을 hashmap에 넣는다.
    1~4를 반복한다.

    # 위의 경우 N^2

    # 완전 탐색: N^3
        # 3000 * 2999 * 2998 =
        # 27,000,000,000
"""

nums = [-1, 0, 1, 2, -1, -4]
answer = set()

for i in range(len(nums) - 2):  # N
    target_num = 0 - nums[i]
    hashmap = {}

    for j in range(i + 1, len(nums)):  # N
        if hashmap:
            sub_target_num = target_num - nums[j]
            if sub_target_num in hashmap:
                answer_candidate = [nums[i], nums[j], sub_target_num]
                answer_candidate.sort()
                answer.add(tuple(answer_candidate))
            if nums[j] not in hashmap:
                hashmap[nums[j]] = 1
        else:
            hashmap[nums[j]] = 1

answer = [list(x) for x in answer]


# https://leetcode.com/problems/3sum/solutions/2602454/python-solution-100-explained/

nums = [-1, 0, 1, 2, -1, -4]
nums.sort()  # sorting cause we need to avoid duplicates, with this duplicates will be near to each other
l = []
for i in range(len(nums)):  # this loop will help to fix the one number i.e, i
    if i > 0 and nums[i - 1] == nums[i]:  # skipping if we found the duplicate of i
        continue

    # NOW FOLLOWING THE RULE OF TWO POINTERS AFTER FIXING THE ONE VALUE (i)
    j = i + 1  # taking j pointer larger than i (as said in ques)
    k = len(nums) - 1  # taking k pointer from last
    while j < k:
        s = nums[i] + nums[j] + nums[k]
        if (
            s > 0
        ):  # if sum s is greater than 0(target) means the larger value(from right as nums is sorted i.e, k at right)
            # is taken and it is not able to sum up to the target
            k -= 1  # so take value less than previous
        elif (
            s < 0
        ):  # if sum s is less than 0(target) means the shorter value(from left as nums is sorted i.e, j at left)
            # is taken and it is not able to sum up to the target
            j += 1  # so take value greater than previous
        else:
            l.append(
                [nums[i], nums[j], nums[k]]
            )  # if sum s found equal to the target (0)
            j += 1
            while (
                nums[j - 1] == nums[j] and j < k
            ):  # skipping if we found the duplicate of j and we dont need to check
                # the duplicate of k cause it will automatically skip the duplicate by the adjustment of i and j
                j += 1
return l
