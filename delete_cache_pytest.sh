#!/bin/bash

FOLDERS=`find $(pwd) -type d -name ".pytest_cache" && find $(pwd) -type d -name "__pycache__"`

if [ -z "${FOLDERS}" ];
then
	echo "Не найдены папки: .pytest_cache, __pycache__"
else
	echo "Начинаю удаление папок: .pytest_cache, __pycache__"
	for folder in $FOLDERS
	do
		`rm -r $folder`
		echo "Удаление папки - $folder"
	done
	echo "Папки: .pytest_cache, __pycache__ удалены"
fi

