## XHPL Install and Run guide

 1. Install MKL and openmpi

        sudo apt install intel-mkl-full openmpi-bin

 2. Make a copy of Makefile

        cp Make.CUDA Make.is10

 3. Edit the directories to match host system

        nano Make.is10
    >TOPdir = /home/is-10/Desktop/IS_10/20.04/xhpl/hpl-2.0_FERMI_v15

 4. Edit source code to fix legacy code

	    nano src/comm/HPL_packL.c
	  > Replace `MPI_Address` with `MPI_Get_address` @ line 172, 186 & 200
	  > 
	  > Replace `MPI_Type_struct` with `MPI_Type_create_struct` @ line 211

 5. Compile

	    make arch=is10

 6. Move xhpl executable to is10 dir & copy HPL.dat

	    mv bin/CUDA/xhpl bin/is10/xhpl
	    cp bin/CUDA/HPL.dat bin/is10/HPL.dat

 7. Go to is10 dir

	    cd bin/is10

 8. Link the libraries

	    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/is-10/Desktop/IS_10/20.04/xhpl/hpl-2.0_FERMI_v15/src/cuda
	    ldd xhpl

 9. Run the benchmark

	    mpirun -np 4 xhpl
