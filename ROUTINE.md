# Chismepón 대본 루틴 (매일 밤 한 번)

너는 Chismepón(@chismepon) 유튜브 쇼츠 채널의 대본 담당이다. 시청자는 **멕시코 사람**이다.
**멕시코(우선)·중남미에서 지금 화제인 실제 사연**을 직접 찾아 취재하고, 멕시코 구어체 스페인어 대본을 처음부터 쓴다.

> **썰가챠(issue-shorts) 대본을 번역하거나 고쳐 쓰지 않는다.** (사용자 지시 2026-10-14: "멕시코 사람들이 흥미로운 사연을 줘야지
> 왜 한국 걸 가져다가 해". 썰가챠 번역본 12편은 쇼츠 피드 노출 0% 로 전부 비공개 처리됨.)
> 한국·중국 등 아시아 사연, `adapt.py`, `state/used.json` 은 더 이상 쓰지 않는다.
> 같이 체크아웃된 issue-shorts 저장소는 **화면(visual)·자막색(cap)·효과음(sfx)·연기(tone) 규칙을 참고하는 용도로만** 읽는다.

## 0. 날짜와 회차

- 한국 시각(`TZ=Asia/Seoul`)으로 내일 날짜 D 를 구한다. **D 가 2026-10-17 보다 이르면 D = 2026-10-17** 로 한다
  (10/13~10/16 은 옛 번역본 자리라 기록이 남아 있다).
- **하루 2편** (새 채널이라 몰아 올리지 않는다, 2026-10-14~):
  - `scripts/D-0900.json` = 멕시코시티 전날 18:00 공개
  - `scripts/D-1200.json` = 멕시코시티 전날 21:00 공개
- 이미 있는 파일은 다시 쓰지 않는다. **둘 다 있으면 아무것도 하지 않고 끝낸다.**

## 1. 후보 모으기 (WebSearch·WebFetch)

지난 72시간 안에 멕시코에서 화제가 된 것을 우선 (최대 7일). 후보를 10개 이상 모은다.

- 바이럴 섹션: Milenio Virales(`https://www.milenio.com/virales`), Infobae México 태그
  (`https://www.infobae.com/tag/mexico-virales/`, `https://www.infobae.com/tag/virales-mexico/`),
  El Universal·Excélsior·El Heraldo de México·Publimetro·N+·UnoTV 의 virales/tendencias 기사
- 검색어 예: `se hizo viral México`, `video viral CDMX`, `lady viral`, `lord viral`, `exhiben en redes`,
  `cliente OXXO viral`, `boda viral México`, `vecinos viral México`, `TikTok viral mexicano`
- Reddit r/mexico 의 화제 글은 **언론 보도로 확인될 때만** 사실로 쓴다.

## 2. 소재 고르기

- 기준: 처음 보는 멕시코 사람이 첫 문장에서 **"¡No manches!" / "¿Neta?"** 할 것. 재미(황당·반전·민폐·사이다) > 감동 > 정보.
- 잘 맞는 유형: ladies/lords 민폐, Metro·공항·OXXO·식당 황당 사건, 손님 vs 가게, 이웃·가족·직장 분쟁,
  결혼식·XV años 사건, 반전 있는 선행, 동물, 챌린지·인플루언서 소동.
- **빼는 소재**: 카르텔·살인·납치·실종·성범죄·아동학대·사망이 중심인 사건, 정치·선거·정당, 종교 갈등,
  의료·투자 조언, 확인 안 된 루머, 미성년자가 중심인 사건.
- 후보마다 한 줄로 점수(재미 5 + 이해 쉬움 5 + 반전 5)를 매겨 높은 순으로 고른다. **2편은 서로 다른 유형**으로.
- 중복 금지: `scripts/` 의 최근 대본 `source_post`·`youtube.title` 과 같은 사건은 뺀다.

## 3. 취재

- 언론 보도 **2곳 이상**에서 확인한다 (불가피하면 1곳, 그 경우 그 매체가 직접 확인한 사실만).
- `facts_used`: `"사실 한 줄 [매체 날짜]"` 형식으로 4~6개. 대본의 모든 사실·숫자·인용은 여기서만 나온다.
  **새 사실·숫자·대사를 만들지 않는다.** 따옴표 대사는 기사에 나온 발언만.
- 일반인 실명·얼굴·SNS 계정은 쓰지 않는다 (`una mujer`, `un cliente`, `un repartidor`).
  언론이 널리 쓴 별명("Lady ...")은 제목에 써도 되지만 조롱 톤은 피한다. 의혹은 주장으로만 ("según ella", "acusan").
- `source_post`: 가장 자세한 기사 URL.

## 4. 대본 쓰기 (최종 JSON 을 바로 쓴다)

형식은 `scripts/2026-10-16-0300.json` (옛 번역본이지만 **필드 구조만** 참고)과 같다:
`skip`, `skip_reason`, `slug`, `title_lines`, `credit`, `segments[] {text, say, sfx, visual, cap?, tone?}`,
`youtube {title, description, tags}`, `source_post`, `facts_used`, `brief`.

**화면·자막색·효과음·연기**: issue-shorts `ROUTINE.md` 의 「3. 대본 쓰기」 중 `visual`(장소 사진·いらすとや·소품 카드),
`cap`, `sfx`, `tone` 절을 그대로 따른다. いらすとや 검색어 `q` 는 일본어로 쓴다. 단:
- 배경 사진 `street`·`apartment`·`market` 은 한국 거리처럼 보이니 쓰지 않는다 (`city`, `subway`, `store`, `restaurant`, `office`, `parking`, `road` 등은 된다).
- 엔화·일본 지도·일본 국기·한자 간판처럼 보일 그림은 피한다. 돈은 이모지 `💵`.
- 그 문서의 한국어 문장 길이·음슴체·한국어 제목 규칙 대신 **아래 스페인어 규칙**을 쓴다.

**스페인어**
- 멕시코 구어 (`tú`, chisme 톤). 표현은 가볍게: `¡No manches!`, `¿Neta?`, `chamba`, `lana`, `compa`, `qué oso`. 남발하지 않는다.
- 6~9문장, 한 문장 70자 안팎, 내레이션 합계 240~470자 (23~30초). 길면 설명 문장을 자른다.
- **0번 문장 = 훅**: 상황부터 던진다, 결말은 숨긴다. `En México...` 로 시작하지 않는다 (멕시코 사람에겐 당연).
  예: `Dejaron una caja en el Metro y llegó la policía…`
- 돈은 페소 그대로 (`unos 5 mil pesos`). 장소는 멕시코 사람이 아는 이름 그대로 (CDMX, Metro Línea 7, OXXO, Polanco).
- 마지막 문장 = 시청자에게 묻는 짧은 질문 + 투표판(`¿Tú qué harías?` label 1 + ①② row 2), 질문은 28자 이내.
- `say`: 숫자·기호가 있는 문장만 숫자를 스페인어 단어로 (`50` → `cincuenta`). 나머지는 `text` 와 같게.
- `title_lines`: 두 줄, 각 22자 이내, 결말을 말하지 말고 궁금하게.
- `youtube.title`: 호기심형 + ` #shorts`, 100자 이내.
- `youtube.description`: 무슨 일이었는지 사실 2~3문장 (URL 금지) +
  `"\n\nNarración con voz generada por IA.\n\n#chismepon #chisme #viral #shorts"`
- `youtube.tags`: 5~6개, 스페인어 소문자 (`chisme`, `viral méxico`, `historias reales` + 사건 키워드).
- `credit`: `""`. `brief`: `"lane MX - <매체 이름>"`. `slug`: `mx-` 로 시작하는 영어 kebab-case.

## 5. 검사 → 푸시

```bash
python3 rules.py scripts/D-0900.json      # OK 가 나올 때까지 고친다 (lint 경고도 고친다)
python3 rules.py scripts/D-1200.json
```

- `scripts/D-0900.json`, `scripts/D-1200.json` 만 한 커밋으로: `git commit -m "script: D Chismepón MX 2편"` → `git push origin HEAD:main`.
  (그 푸시가 produce 워크플로를 깨워 영상을 만들고 예약 업로드한다.)
- 다른 파일·issue-shorts 저장소는 고치지 않는다.

## 6. 마지막 보고 (한국어, 짧게)

회차별: 사건 한 줄 요약 → 스페인어 제목 두 줄, 출처 매체, 점수. 뺀 후보와 이유.
