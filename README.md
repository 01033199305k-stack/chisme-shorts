# chisme-shorts

**Chismepón** (@chismepon) - 썰가챠(issue-shorts) 파이프라인의 스페인어(라틴아메리카) 판.
같은 썰을 스페인어 구어체로 다시 쓰고, 소희(Qwen3-TTS CustomVoice) 목소리가 스페인어로 읽는다.

- 1차 시험 10편: `batch1/` (썰가챠 대본의 그림·효과는 그대로, 글만 교체 - `python batch1/build.py`)
- 렌더: `python run.py --script batch1/03-....json --dry-run` (PC 는 config.local.yaml 로 Voicebox 소희)
- 업로드: 하루 4편, 멕시코시티 12·15·18·21시 = 한국 03·06·09·12시 예약 공개
  - 1차분: `python upload/run.py --day 1` (Aside 브라우저로 스튜디오 예약)
- 스톡 영상: Pixabay 키를 `.pixabay_key` (gitignore) 또는 시크릿 PIXABAY_API_KEY 로
- 비밀값: `python setup.py` (Chismepón 전용 Google Cloud 프로젝트의 OAuth 클라이언트)

폰트: Anton·Archivo Black (OFL, assets/fonts) - 한글 폰트에는 á·ñ·¿ 글자가 없다.
