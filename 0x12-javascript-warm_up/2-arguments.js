#!/usr/bin/node

const argc = process.argv.length - 2;

if (argc === 0) { console.log('No argument'); }

if (argc === 1) { console.log('Argument found'); }

if (argc > 1) { console.log('Arguments found'); }
