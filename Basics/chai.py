from hello import chai
chai("Lemon tea")

#after this one folder will be created named __pycache__
# !Python Inner working
# ^ Firstly python creates byte code -> python virtual machine is also intalled when we install python
# ^ code goes into python vm then the code gets executed
# ^byte code is low level code. It is platform independent so it can be used on different platforms
# ^ Byte code is comaparately faster than script code
# ^ .pyc -> compiled python(these are also called - Frozen binaries)
# ^ Byte code is not machine code it is python specific interpretation here 
# ^__pycache__ -> the more we make changes in our code frozen binaries are reconstructed
# ^ adn thus this will create several files that's why __pycachce__ file is created to organise these things
# ^ __pycache__
# ^ source change and python version
# ^ when me make changes in our source code then python uses diffing algorithms
# ^ diffing algos -> differernce finding algorithms
# ^ so it only pushes the changes in the file not the entire source code
# ^312 is just a version of python and it uses standard python of cpython
# ^ works only for imported files and not for top level files
# ^ different python versions -> jpython, Iron python , Stackless(concurrency), pypy(performance oriented)

#! this is the reason why python is called interpretted langauge