#!/usr/bin/env python

import sys
import os
import glob

from build_tools.util import RunOrDie

def BuildOniOS():
  RunOrDie(['xcodebuild', '-project', 'base/base.xcodeproj', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'composer/composer.xcodeproj', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'config/config.xcodeproj', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'converter/converter.xcodeproj', '-configuration', "Release", '-target', "converter"])
  RunOrDie(['xcodebuild', '-project', 'converter/converter_base.xcodeproj', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'data_manager/data_manager.xcodeproj', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'data_manager/oss/oss_data_manager.xcodeproj', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'data_manager/oss/oss_data_manager_base.xcodeproj', '-configuration', "Release", '-target', "All"])

  # workaround for __LINKEDIT error
  RunOrDie(['xcodebuild', '-project', 'dictionary/dictionary.xcodeproj', '-configuration', "Release", '-target', "All", "COPY_PHASE_STRIP=NO"])

  RunOrDie(['xcodebuild', '-project', 'dictionary/dictionary.xcodeproj', '-configuration', "Release", '-target', "All"])

  RunOrDie(['xcodebuild', '-project', 'dictionary/dictionary_base.xcodeproj', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'dictionary/file/dictionary_file.xcodeproj', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'dictionary/system/system_dictionary.xcodeproj', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'engine/engine.xcodeproj', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'prediction/prediction.xcodeproj', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'prediction/prediction_base.xcodeproj', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'protobuf/protobuf.xcodeproj', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'rewriter/rewriter.xcodeproj', '-configuration', "Release", '-target', "rewriter"])
  RunOrDie(['xcodebuild', '-project', 'rewriter/rewriter_base.xcodeproj', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'rewriter/calculator/calculator.xcodeproj', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'session/session.xcodeproj', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'session/session_base.xcodeproj', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'storage/storage.xcodeproj', '-configuration', "Release", '-target', "storage"])
  RunOrDie(['xcodebuild', '-project', 'storage/louds/louds.xcodeproj', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'transliteration/transliteration.xcodeproj', '-configuration', "Release", '-target', "transliteration"])
  RunOrDie(['xcodebuild', '-project', 'usage_stats/usage_stats.xcodeproj', '-configuration', "Release", '-target', "usage_stats_uploader"])
  RunOrDie(['xcodebuild', '-project', 'usage_stats/usage_stats_base.xcodeproj', '-configuration', "Release", '-target', "All"])

def BuildOniOSSimulator():
  RunOrDie(['xcodebuild', '-project', 'base/base.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'composer/composer.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'config/config.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'converter/converter.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "converter"])
  RunOrDie(['xcodebuild', '-project', 'converter/converter_base.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'data_manager/data_manager.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'data_manager/oss/oss_data_manager.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'data_manager/oss/oss_data_manager_base.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "All"])

  # workaround for __LINKEDIT error
  RunOrDie(['xcodebuild', '-project', 'dictionary/dictionary.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "All", "COPY_PHASE_STRIP=NO"])

  RunOrDie(['xcodebuild', '-project', 'dictionary/dictionary.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "All"])

  RunOrDie(['xcodebuild', '-project', 'dictionary/dictionary_base.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'dictionary/file/dictionary_file.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'dictionary/system/system_dictionary.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'engine/engine.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'prediction/prediction.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'prediction/prediction_base.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'protobuf/protobuf.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'rewriter/rewriter.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "rewriter"])
  RunOrDie(['xcodebuild', '-project', 'rewriter/rewriter_base.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'rewriter/calculator/calculator.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'session/session.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'session/session_base.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'storage/storage.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "storage"])
  RunOrDie(['xcodebuild', '-project', 'storage/louds/louds.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "All"])
  RunOrDie(['xcodebuild', '-project', 'transliteration/transliteration.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "transliteration"])
  RunOrDie(['xcodebuild', '-project', 'usage_stats/usage_stats.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "usage_stats_uploader"])
  RunOrDie(['xcodebuild', '-project', 'usage_stats/usage_stats_base.xcodeproj', '-sdk', 'iphonesimulator', '-configuration', "Release", '-target', "All"])

def merge():
  libfiles = glob.glob("./out_ios/Release-iphoneos/*.a")
  for filepath in libfiles:
    filename = os.path.split(filepath)[1]
    RunOrDie([
      'xcrun', '-sdk', 'iphoneos', 'lipo', '-create',
      './out_ios/Release-iphoneos/' + filename,
      './out_ios/Release-iphonesimulator/' + filename,
      '-output',
      './out_ios/Release-merged/' + filename
    ])
    # os.remove('./out_ios/Release-iphonesimulator/' + filename)

if __name__ == '__main__':
  BuildOniOS()
  BuildOniOSSimulator()
  merge()
