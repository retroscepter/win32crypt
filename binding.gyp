{
  "targets": [
    {
      "target_name": "win32crypt",
      "sources": [ "native/win32crypt.cpp" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "include"
      ],
      "libraries": [
        "-lcrypt32.lib"
      ]
    }
  ]
}