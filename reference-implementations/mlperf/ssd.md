## SSD Install and Run guide

1.  Change method of installing apex
    

	a.  Remove from requirements.txt
    

		git+git://github.com/NVIDIA/apex.git@9041a868a1a253172d94b113a963375b9badd030#egg=apex

	b.  Add to Dockerfile
    

		pip install git+git://github.com/NVIDIA/apex.git@9041a868a1a253172d94b113a963375b9badd030#egg=apex --global-option="--cpp_ext" --global-option="--cuda_ext"

2.  Download the ‘COCO 2017 train and val’ data set
    

		./download_dataset.sh

3.  Download resnet34 backbone
    

		./download_resnet34_backbone.sh

4.  Convert backbone PTH file to pickle
    

		python3 pth_to_pickle.py resnet34-333f7ec4.pth resnet34-333f7ec4.pickle

5.  Edit ‘run.sub’ file
    

	a.  Replace
    

		DATADIR=${DATADIR:-"/raid/data/coco-2017"}  # there should be ./coco2017 and ./torchvision dirs in here  
		LOGDIR=${LOGDIR:-"/raid/results/$BENCHMARK"}

	>with

		DATADIR=${DATADIR:-"/coco"}  # there should be ./coco2017 and ./torchvision dirs in here  
		LOGDIR=${LOGDIR:-"/coco/results/$BENCHMARK"}

7.  Edit ‘config_DGX1.sh’ file to match the system environment.
    
8.  Build docker image
    

		docker build -t mlperf-nvidia:single_stage_detector .

9.  Run benchmark with the following command
    

		./run.sub
