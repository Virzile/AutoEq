# -*- coding: utf-8 -*-

import os
import sys
import argparse
sys.path.insert(1, os.path.realpath(os.path.join(sys.path[0], os.pardir)))
from autoeq import batch_processing

ROOT_DIR = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--new_only', action='store_true', help='Process only new measurements?')
    arg_parser.add_argument('--innerfidelity', action='store_true', help='Process Innerfidelity measurements?')
    arg_parser.add_argument('--headphonecom', action='store_true', help='Process Headphone.com measurements?')
    arg_parser.add_argument('--oratory1990', action='store_true', help='Process oratory1990 measurements?')
    arg_parser.add_argument('--rtings', action='store_true', help='Process Rtings measurements?')
    arg_parser.add_argument('--referenceaudioanalyzer', action='store_true',
                            help='Process Reference Audio Analyzer measurements?')
    arg_parser.add_argument('--crinacle', action='store_true', help='Process Crinacle measurements?')
    arg_parser.add_argument('--onear', action='store_true', help='Process on-ear measurements?')
    arg_parser.add_argument('--inear', action='store_true', help='Process in-ear measurements?')
    arg_parser.add_argument('--earbud', action='store_true', help='Process ear bud measurements?')
    cli_args = arg_parser.parse_args()

    new_only = bool(cli_args.new_only)
    innerfidelity = bool(cli_args.innerfidelity)
    headphonecom = bool(cli_args.headphonecom)
    oratory1990 = bool(cli_args.oratory1990)
    rtings = bool(cli_args.rtings)
    referenceaudioanalyzer = bool(cli_args.referenceaudioanalyzer)
    crinacle = bool(cli_args.crinacle)

    onear = bool(cli_args.onear)
    inear = bool(cli_args.inear)
    earbud = bool(cli_args.earbud)

    if not innerfidelity and not headphonecom and not oratory1990 and not rtings and not referenceaudioanalyzer and not crinacle:
        innerfidelity = True
        headphonecom = True
        oratory1990 = True
        rtings = True
        referenceaudioanalyzer = True
        crinacle = True
    if not onear and not inear and not earbud:
        onear = True
        inear = True
        earbud = True

    innerfidelity_overear = os.path.join(ROOT_DIR, 'measurements', 'innerfidelity', 'resources', 'innerfidelity_ief_neutral_over-ear.csv')
    innerfidelity_inear = os.path.join(ROOT_DIR, 'measurements', 'innerfidelity', 'resources', 'innerfidelity_ief_neutral_in-ear.csv')
    headphonecom_overear = os.path.join(ROOT_DIR, 'measurements', 'headphonecom', 'resources', 'headphonecom_ief_neutral_over-ear.csv')
    headphonecom_inear = os.path.join(ROOT_DIR, 'measurements', 'headphonecom', 'resources', 'headphonecom_ief_neutral_in-ear.csv')
    rtings_overear = os.path.join(ROOT_DIR, 'measurements', 'rtings', 'resources', 'rtings_ief_neutral_over-ear.csv')
    rtings_inear = os.path.join(ROOT_DIR, 'measurements', 'rtings', 'resources', 'rtings_ief_neutral_in-ear.csv')
    ief_inear = os.path.join(ROOT_DIR, 'compensation', 'ief_neutral_in-ear.csv')
    ief_overear = os.path.join(ROOT_DIR, 'compensation', 'ief_neutral_over-ear.csv')
    crinacle_ears711_overear = os.path.join(ROOT_DIR, 'measurements', 'crinacle', 'resources', 'crinacle_ears-711_ief_neutral_over-ear.csv')
    #measurements/referenceaudioanalyzer/resources/referenceaudioanalyzer_hdm1_ief_neutral_over-ear.csv
    raa_hdmx = os.path.join(ROOT_DIR, 'measurements', 'referenceaudioanalyzer', 'resources', 'referenceaudioanalyzer_hdm-x_ief_neutral_over-ear.csv')
    raa_hdm1 = os.path.join(ROOT_DIR, 'measurements', 'referenceaudioanalyzer', 'resources', 'referenceaudioanalyzer_hdm1_ief_neutral_over-ear.csv')
    raa_siec = os.path.join(ROOT_DIR, 'measurements', 'referenceaudioanalyzer', 'resources', 'referenceaudioanalyzer_siec_ief_neutral_in-ear.csv')

    eq_kwargs = {
        'equalize': True, 'parametric_eq': True, 'max_filters': [5, 5], 'ten_band_eq': True, 'new_only': new_only,
        'convolution_eq': True, 'fs': [44100, 48000]
    }
    onear_kwargs = eq_kwargs.copy()
    onear_kwargs.update({'bass_boost_gain': 4.0})
    inear_kwargs = eq_kwargs.copy()
    inear_kwargs.update({'bass_boost_gain': 6.0})
    earbud_kwargs = eq_kwargs.copy()
    earbud_kwargs.update({'bass_boost_gain': 0.0})

    if innerfidelity:
        if onear:
            print('\nProcessing Innerfidelity on-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'innerfidelity', 'data', 'onear'),
                output_dir=os.path.join(ROOT_DIR, 'results_ief_with_bass', 'innerfidelity', 'innerfidelity_ief_neutral_over-ear'),
                compensation=innerfidelity_overear,
                **onear_kwargs
            )

        if inear:
            print('\nProcessing Innerfidelity in-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'innerfidelity', 'data', 'inear'),
                output_dir=os.path.join(ROOT_DIR, 'results_ief_with_bass', 'innerfidelity', 'innerfidelity_ief_neutral_in-ear'),
                compensation=innerfidelity_inear,
                **inear_kwargs
            )

        if earbud:
            print('\nProcessing Innerfidelity earbud measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'innerfidelity', 'data', 'earbud'),
                output_dir=os.path.join(ROOT_DIR, 'results_ief_with_bass', 'innerfidelity', 'innerfidelity_ief_neutral_in-ear'),
                compensation=innerfidelity_inear,
                **earbud_kwargs
            )

    if headphonecom:
        if onear:
            print('\nProcessing Headphone.com on-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'headphonecom', 'data', 'onear'),
                output_dir=os.path.join(ROOT_DIR, 'results_ief_with_bass', 'headphonecom', 'headphonecom_ief_neutral_over-ear'),
                compensation=headphonecom_overear,
                **onear_kwargs
            )

        if inear:
            print('\nProcessing Headphone.com in-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'headphonecom', 'data', 'inear'),
                output_dir=os.path.join(ROOT_DIR, 'results_ief_with_bass', 'headphonecom', 'headphonecom_ief_neutral_in-ear'),
                compensation=headphonecom_inear,
                **inear_kwargs
            )

        if earbud:
            print('\nProcessing Headphone.com earbud measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'headphonecom', 'data', 'earbud'),
                output_dir=os.path.join(ROOT_DIR, 'results_ief_with_bass', 'headphonecom', 'headphonecom_ief_neutral_in-ear'),
                compensation=headphonecom_inear,
                **earbud_kwargs
            )

    if oratory1990:
        if onear:
            print('\nProcessing oratory1990 on-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'oratory1990', 'data', 'onear'),
                output_dir=os.path.join(ROOT_DIR, 'results_ief_with_bass', 'oratory1990', 'ief_neutral_over-ear'),
                compensation=ief_overear,
                **onear_kwargs
            )

        if inear:
            print('\nProcessing oratory1990 in-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'oratory1990', 'data', 'inear'),
                output_dir=os.path.join(ROOT_DIR, 'results_ief_with_bass', 'oratory1990', 'ief_neutral_in-ear'),
                compensation=ief_inear,
                **inear_kwargs
            )

        if earbud:
            print('\nProcessing oratory1990 ear bud measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'oratory1990', 'data', 'earbud'),
                output_dir=os.path.join(ROOT_DIR, 'results_ief_with_bass', 'oratory1990', 'ief_neutral_in-ear'),
                compensation=ief_inear,
                **earbud_kwargs
            )

    if rtings:
        if onear:
            # Rtings on-ear Avg
            print('\nProcessing Rtings on-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'rtings', 'data', 'onear'),
                output_dir=os.path.join(ROOT_DIR, 'results_ief_with_bass', 'rtings', 'rtings_ief_neutral_over-ear'),
                compensation=rtings_overear,
                **onear_kwargs
            )

        if inear:
            print('\nProcessing Rtings in-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'rtings', 'data', 'inear'),
                output_dir=os.path.join(ROOT_DIR, 'results_ief_with_bass', 'rtings', 'rtings_ief_neutral_in-ear'),
                compensation=rtings_inear,
                **inear_kwargs
            )

        if earbud:
            print('\nProcessing Rtings earbud measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'rtings', 'data', 'earbud'),
                output_dir=os.path.join(ROOT_DIR, 'results_ief_with_bass', 'rtings', 'rtings_ief_neutral_in-ear'),
                compensation=rtings_inear,
                **earbud_kwargs
            )

    if referenceaudioanalyzer:
        if onear:
            print('\nProcessing Reference Audio Analyzer HDM-X on-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'referenceaudioanalyzer', 'data', 'onear', 'HDM-X'),
                output_dir=os.path.join(ROOT_DIR, 'results_ief_with_bass', 'referenceaudioanalyzer', 'referenceaudioanalyzer_hdm-x_ief_neutral_over-ear'),
                compensation=raa_hdmx,
                **onear_kwargs
            )
            print('\nProcessing Reference Audio Analyzer HDM1 on-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'referenceaudioanalyzer', 'data', 'onear', 'HDM1'),
                output_dir=os.path.join(ROOT_DIR, 'results_ief_with_bass', 'referenceaudioanalyzer', 'referenceaudioanalyzer_hdm1_ief_neutral_over-ear'),
                compensation=raa_hdm1,
                **onear_kwargs
            )
        if inear:
            print('\nProcessing Reference Audio Analyzer SIEC in-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'referenceaudioanalyzer', 'data', 'inear', 'SIEC'),
                output_dir=os.path.join(ROOT_DIR, 'results_ief_with_bass', 'referenceaudioanalyzer', 'referenceaudioanalyzer_siec_ief_neutral_in-ear'),
                compensation=raa_siec,
                **inear_kwargs
            )
            print('\nProcessing Reference Audio Analyzer SIEC CUSTOM in-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'referenceaudioanalyzer', 'data', 'inear', 'SIEC CUSTOM'),
                output_dir=os.path.join(ROOT_DIR, 'results_ief_with_bass', 'referenceaudioanalyzer', 'referenceaudioanalyzer_siec_ief_neutral_in-ear'),
                compensation=raa_siec,
                **inear_kwargs
            )
        if earbud:
            print('\nProcessing Reference Audio Analyzer SIEC earbud measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'referenceaudioanalyzer', 'data', 'earbud', 'SIEC'),
                output_dir=os.path.join(ROOT_DIR, 'results_ief_with_bass', 'referenceaudioanalyzer', 'referenceaudioanalyzer_siec_ief_neutral_in-ear'),
                compensation=raa_siec,
                **earbud_kwargs
            )

    if crinacle:
        if onear:
            print('\nProcessing Crinacle Ears-711 on-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'crinacle', 'data', 'onear', 'Ears-711'),
                output_dir=os.path.join(ROOT_DIR, 'results_ief_with_bass', 'crinacle', 'ears-711_ief_neutral_over-ear'),
                compensation=crinacle_ears711_overear,
                **onear_kwargs
            )
            print('\nProcessing Crinacle GRAS 43AG-7 on-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'crinacle', 'data', 'onear', 'GRAS 43AG-7'),
                output_dir=os.path.join(ROOT_DIR, 'results_ief_with_bass', 'crinacle', 'gras_43ag-7_ief_neutral_over-ear'),
                compensation=ief_overear,
                **onear_kwargs
            )
        if inear:
            print('\nProcessing Crinacle in-ear measurements...')
            batch_processing(
                input_dir=os.path.join(ROOT_DIR, 'measurements', 'crinacle', 'data', 'inear'),
                output_dir=os.path.join(ROOT_DIR, 'results_ief_with_bass', 'crinacle', 'ief_neutral_in-ear'),
                compensation=ief_inear,
                **inear_kwargs
            )


if __name__ == '__main__':
    main()
