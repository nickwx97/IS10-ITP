#!/bin/bash

for i in {1..10}
do
	echo "#$i run start"
	hashcat -b > hashcat/hashcat\-$i
	echo "#$i run end"
done
