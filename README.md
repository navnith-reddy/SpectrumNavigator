# Spectrum Navigator

Spectrum Navigator is a spectrum data management tool developed for the Australian Communication and Media Authority (ACMA). Spectrum Navigator is capable of providing Register of Radiocommunication Licence (RRL) extracts and holdings summaries of any given client. Extracts and holdings summaries are provided in the form a csv file and shapefile. Spectrum Navigator is also capable of retrieving information from the ACMA's Register of Radiocommunication Licences (RRL) and Australian Spectrum Map Grid (ASMG) to build a queryable geodatabase which facilitates the production of client shape files, kml files and data extracts.

Spectrum Navigator is accompanied by two spectrum management libraries that provide extended functionality such as unique Hierarchial Cell Identifier Scheme (HCIS) sequence detection, HCIS to shapefile conversion, build and compilation of primary ASMG and RRL files and automated database retrieval.

## Licence Extract

The licence extract feature takes licence numbers, searches the RRL and generates a shapefile based on the associated HCIS IDs. Multiple licence number inputs will be grouped to distinguish licence areas.

## Client Extract

The client extract feature takes a client ID, searches the RRL and generates a shapefile based on associated HCIS IDs. Unlike the licence extract, the client extract will also feature a client summary.

## Holdings Summary

## Shapefile to HCIS Cell
