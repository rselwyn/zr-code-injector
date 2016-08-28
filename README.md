# Zero Robotics Code Injector

Currently, the Zero Robotics code can only be compiled and run online.  This tool will save you time because it will make your Zero Robotics code runnable on the desktop.

# Run

To compile and run your ZR code, use

```
python injector.py <zr-file.cpp>
```

# Installing the Stand Alone Compiler

In the executable directory, run

```
cp zr-compile.py /usr/local/bin/zr-compile
cd /usr/local/bin
chmod 555 zr-compile
```

To use the stand alone compiler, run

```
zr-compile <file-name>
```

If you would like to remove the artifacts (`a.out` and the `COMPILED-*` file), use

```
zr-compile <file-name> clean
```