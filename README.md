Mozc-for-iOS [![Apache License 2.0](https://img.shields.io/badge/license-Apache%202.0-yellow.svg?style=flat)](https://www.tldrlegal.com/l/apache2)
============

Mozc for iOS build
forked from https://github.com/kishikawakatsumi/Mozc-for-iOS

### Credits

https://code.google.com/p/mozc/

### References

https://code.google.com/p/mozc/

### System Requirements

    macOS 10.15 Catalina
    Xcode 10
    iOS SDK 12
    Python 2.7.10
    
### Tested Environments

    iPhone SE, iOS Simulator 13.4


### Get the Code

```
$ git clone https://github.com/yusakuw/Mozc-for-iOS.git mozc_ios
```

### Build Instructions

#### Configuration

```
$ cd mozc_ios/src
$ python build_mozc.py gyp
```

#### Compilation

```
$ python build_mozc_ios.py
```

#### Artifacts

See `src/out_ios/Release-iphoneos`

### Limitation

~~Device build only, cannot run on the simulator.~~  
Now you can run your mozc-enabled apps on the iOS simulators.

### Sample Project

See https://github.com/yusakuw/JapaneseKeyboardKit

 
[Apache]: http://www.apache.org/licenses/LICENSE-2.0
[MIT]: http://www.opensource.org/licenses/mit-license.php
[GPL]: http://www.gnu.org/licenses/gpl.html
[BSD]: http://opensource.org/licenses/bsd-license.php

## License

Mozc-for-iOS is available under the [Apache license][Apache] (same as the original). See the LICENSE file for more info.
