## Minigo Install and Run guide

1.  Change directory to the appropriate directory
    

		cd minigo/implementations/tensorflow

3.  Make a copy of the config file (we used the config_DGX1.sh as a baseline)
    

		cp config_DGX1.sh config_is10.sh

4.  Modify the configuration file to match the system environment
    
5.  Build Docker
    

		nvidia-docker build -t mlperf-nvidia:minigo .

6.  Create checkpoint directory to save checkpoints & log directory to save logs
    

		mkdir checkpoint  
		mkdir logdir

7.  Launch docker container to download dataset
    

		nvidia-docker run -v /mnt/md0/training_results_v0.7/NVIDIA/benchmarks/minigo/implementations/tensorflow/checkpoint:/data --rm -it mlperf-nvidia:minigo

  
		cd minigo  
		gsutil cp gs://minigo-pub/ml_perf/0.7/checkpoint.tar.gz .  
		tar xfz checkpoint.tar.gz -C ml_perf/  
		mkdir -p ml_perf/target/  
		gsutil cp gs://minigo-pub/ml_perf/0.7/target.* ml_perf/target/

8.  Comment out Line 331 in dual_net.py before running freeze_graph to freeze target model
    

		CUDA_VISIBLE_DEVICES=0 python3 freeze_graph.py --flagfile=ml_perf/flags/19/architecture.flags --model_path=ml_perf/target/target

  
		mv ml_perf/target/target.minigo ml_perf/target/target.minigo.tf

9.  Uncomment Line 331 in dual_net.py, then copy the dataset to /data. Exit docker after that.
    

		cp -a ml_perf/target /data/  
		cp -a ml_perf/checkpoints/mlperf07 /data/  
		exit

10.  Launch benchmark
	
    CONT="mlperf-nvidia:minigo" DATADIR=/mnt/md0/training_results_v0.7/NVIDIA/benchmarks/minigo/implementations/tensorflow/checkpoint LOGDIR=/mnt/md0/training_results_v0.7/NVIDIA/benchmarks/minigo/implementations/tensorflow/logdir DGXSYSTEM=is10 bash run_with_docker.sh
