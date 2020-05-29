#!/usr/bin/env python
import logging
import time
from engine.engine import Engine
import os


TSHARK_DIR = '/home/researchdev/Desktop/tshark'
PYKEYLOGGER_DIR = '/home/researchdev/Desktop/pykeylogger'
NMAP_DIR = '/home/researchdev/Desktop/nmap'
MANUAL_DIR = '/home/researchdev/Desktop/manuals'
SNOOPY_DIR = '/home/researchdev/Desktop/snoopy'

def execute_tshark_test():
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug("Starting Program")
    logging.debug("Engine_invoker: getting engine instance")
    engine = Engine()
    logging.debug("Engine_invoker: Removing all previous data")
    engine.delete_all()
    logging.debug("Engine_invoker: invoking print_collector_names")
    engine.print_collector_names()
    logging.debug("Engine_invoker: obtaining tshark collector")
    c = engine.get_collector("tshark")
    logging.debug("Engine_invoker: starting collector")
    engine.start_collector(c)
    logging.debug("Engine_invoker: waiting 5 seconds")
    time.sleep(10)
    logging.debug("Engine_invoker: stopping collector")
    engine.stop_collector(c)
    logging.debug("Engine_invoker: parsing data")
    engine.parser(c)
    logging.debug("Engine_invoker: exporting data")
    os.makedirs(TSHARK_DIR, exist_ok=True)
    engine.export(TSHARK_DIR)
    logging.debug("Engine_invoker: Complete. Exiting")

def execute_pykeylogger_test():
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug("Starting Program")
    logging.debug("Engine_invoker: getting engine instance")
    engine = Engine()
    logging.debug("Engine_invoker: Removing all previous data")
    engine.delete_all()
    logging.debug("Engine_invoker: invoking print_collector_names")
    engine.print_collector_names()
    logging.debug("Engine_invoker: obtaining pykeylogger collector")
    c = engine.get_collector("pykeylogger")
    logging.debug("Engine_invoker: starting collector")
    engine.start_collector(c)
    logging.debug("Engine_invoker: waiting 5 seconds")
    time.sleep(10)
    logging.debug("Engine_invoker: stopping collector")
    engine.stop_collector(c)
    logging.debug("Engine_invoker: parsing data")
    engine.parser(c)
    logging.debug("Engine_invoker: exporting data")
    os.makedirs(PYKEYLOGGER_DIR, exist_ok=True)
    engine.export(PYKEYLOGGER_DIR)
    logging.debug("Engine_invoker: Complete. Exiting")

def execute_nmap_test():
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug("Starting Program")
    logging.debug("Engine_invoker: getting engine instance")
    engine = Engine()
    logging.debug("Engine_invoker: Removing all previous data")
    engine.delete_all()
    logging.debug("Engine_invoker: invoking print_collector_names")
    engine.print_collector_names()
    logging.debug("Engine_invoker: obtaining nmap collector")
    c = engine.get_collector("nmap")
    logging.debug("Engine_invoker: starting collector")
    engine.start_collector(c)
    logging.debug("Engine_invoker: waiting 5 seconds")
    time.sleep(10)
    logging.debug("Engine_invoker: stopping collector")
    engine.stop_collector(c)
    logging.debug("Engine_invoker: parsing data")
    engine.parser(c)
    logging.debug("Engine_invoker: exporting data")
    os.makedirs(NMAP_DIR, exist_ok=True)
    engine.export(NMAP_DIR)
    logging.debug("Engine_invoker: Complete. Exiting")

def execute_manualscreenshot_test():
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug("Starting Program")
    logging.debug("Engine_invoker: getting engine instance")
    engine = Engine()
    logging.debug("Engine_invoker: Removing all previous data")
    engine.delete_all()
    logging.debug("Engine_invoker: invoking print_collector_names")
    engine.print_collector_names()
    logging.debug("Engine_invoker: obtaining manualscreenshot collector")
    c = engine.get_collector("manualscreenshot")
    logging.debug("Engine_invoker: starting collector")
    engine.start_collector(c)
    logging.debug("Engine_invoker: waiting 5 seconds")
    time.sleep(10)
    logging.debug("Engine_invoker: stopping collector")
    engine.stop_collector(c)
    logging.debug("Engine_invoker: parsing data")
    engine.parser(c)
    logging.debug("Engine_invoker: exporting data")
    os.makedirs(MANUAL_DIR, exist_ok=True)
    engine.export(MANUAL_DIR)
    logging.debug("Engine_invoker: Complete. Exiting")

def execute_snoopy_test():
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug("Starting Program")
    logging.debug("Engine_invoker: getting engine instance")
    engine = Engine()
    logging.debug("Engine_invoker: Removing all previous data")
    engine.delete_all()
    logging.debug("Engine_invoker: invoking print_collector_names")
    engine.print_collector_names()
    logging.debug("Engine_invoker: obtaining snoopy collector")
    c = engine.get_collector("snoopy")
    logging.debug("Engine_invoker: starting collector")
    engine.start_collector(c)
    logging.debug("Engine_invoker: waiting 5 seconds")
    time.sleep(30)
    logging.debug("Engine_invoker: stopping collector")
    engine.stop_collector(c)
    logging.debug("Engine_invoker: parsing data")
    engine.parser(c)
    logging.debug("Engine_invoker: exporting data")
    os.makedirs(SNOOPY_DIR, exist_ok=True)
    engine.export(SNOOPY_DIR)
    logging.debug("Engine_invoker: Complete. Exiting")

if __name__ == "__main__":
    execute_tshark_test()
    execute_pykeylogger_test()
    execute_nmap_test()
    execute_manualscreenshot_test()
    execute_snoopy_test()
