def solution(genres, plays):
    N = len(genres)
    answer = []
    nums = {}
    cnt = {}

    # 1) 장르별 노래 목록, 장르별 총 재생수 집계
    for i in range(N):
        genre = genres[i]
        nums.setdefault(genre, []).append([i, plays[i]])
        cnt[genre] = cnt.get(genre, 0) + plays[i]

    # 2) 장르 내 정렬: 재생수 내림차순, 고유번호 오름차순
    for genre in nums:
        nums[genre].sort(key=lambda x: (-x[1], x[0]))

    # 3) 장르 정렬: 총 재생수 내림차순
    sorted_genres = sorted(cnt.items(), key=lambda x: x[1], reverse=True)

    # 4) 장르별로 최대 2곡 선택
    for genre, _ in sorted_genres:
        music = nums[genre]
        for i in range(min(2, len(music))):
            answer.append(music[i][0])

    return answer