make gettext (OR) sphinx-build -b gettext . build/gettext

sphinx-intl update -p build/gettext -l it -l es -l lv

export BASE_URL=/en
sphinx-build -b html -D language=es . ../build/html/es
export BASE_URL=/es
sphinx-build -b html -D language=en . ../build/html/en
export BASE_URL=/it
sphinx-build -b html -D language=it . ../build/html/it
export BASE_URL=/lv
sphinx-build -b html -D language=lv . ../build/html/lv


PASOS PARA ALOJAR LA DOCUMENTACIÓN EN READTHEDOCS



PASOS PARA ALOJAR LA DOCUMENTACIÓN EN EL STAGING SERVER

usar el docker-compose.yml