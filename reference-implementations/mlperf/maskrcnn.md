## Mask R-CNN Install and Run guide

1.  Change working directory
    

		cd maskrcnn/implementations/pytorch

3.  Copy config_DGX1.sh as baseline and modify system configurations and DLparams
    

		cp config_DGX1.sh config_is10.sh

4.  Download COCO Dataset and weights.
    

		mkdir -p /coco/coco2017; cd /coco/coco2017  
		curl -O http://images.cocodataset.org/zips/train2017.zip; unzip train2017.zip  
		curl -O http://images.cocodataset.org/zips/val2017.zip; unzip val2017.zip  
		curl -O http://images.cocodataset.org/annotations/annotations_trainval2017.zip; unzip annotations_trainval2017.zip  
  
		mkdir models  
		cd models  
		wget https://dl.fbaipublicfiles.com/detectron/ImageNetPretrained/MSRA/R-50.pkl

5.  Build docker image
    

		cd /mnt/md0/training_results_v0.7/NVIDIA/benchmarks/maskrcnn/implementations/pytorch

		docker build -t nvidia-mlperf:maskrcnn .

6.  Launch benchmark
    

		CONT=nvidia-mlperf:maskrcnn DGXSYSTEM=is10 DATADIR=/coco ./run_with_docker.sh
