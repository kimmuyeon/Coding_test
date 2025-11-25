def solution(participant, completion):
    # 둘다 정렬
    part = sorted(participant)
    comp = sorted(completion)
    
    # 숫자 0에서부터 인덱싱으로 비교, answer 초기값 설정
    versus = 0
    answer = None
    
    # comp의 길이 만큼 반복 (더 적기 때문에)
    while versus < len(comp):     
        if part[versus] != comp[versus]:
            answer = part[versus]
            return answer
        versus += 1
    
    # while 문 돌고난 후 answer 값 기입
    answer = part[versus]
    return part[versus]