export BASE_URL=/en
sphinx-build -b html -D language=es . ../build/html/es
export BASE_URL=/es
sphinx-build -b html -D language=en . ../build/html/en
export BASE_URL=/it
sphinx-build -b html -D language=it . ../build/html/it
export BASE_URL=/lv
sphinx-build -b html -D language=lv . ../build/html/lv