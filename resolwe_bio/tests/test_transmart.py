# pylint: disable=missing-docstring
import unittest
from .utils import ProcessTestCase


class TranSMARTProcessorTestCase(ProcessTestCase):
    @unittest.skip("processor connects to remote tranSMART server")
    def test_import(self):
        self.assertDataCount(0)
        inputs = {'exps': 'transmart_log_exp.xlsx'}
        annotation = self.run_processor('import:web:transmart:expressions', inputs)
        self.assertDataCount(5)
        self.assertFields(annotation, 'expset_type', 'Log2')
        self.assertFileExists(annotation, 'expset')

    @unittest.skip("processor connects to remote tranSMART server")
    def test_import_with_annotation(self):
        self.keep_all()
        inputs = {
            'exps': '/studies/UBIOPRED/concepts/Expression/Affymetrix%20Human%20Genome%20U133%20Plus%202.0%20Array/Lung',
            'ann': '/studies/UBIOPRED/concepts/Sample%20Identifiers/Virology%20Sample%20ID/18_or_more;/studies/UBIOPRED/concepts/Sample%20Identifiers/Virology%20Sample%20ID/2to17;/studies/UBIOPRED/concepts/Sample%20Identifiers/Virology%20Sample%20ID/less_than_2;/studies/UBIOPRED/concepts/Sample%20Identifiers/Baseline%20visit%20kitID/no;/studies/UBIOPRED/concepts/Sample%20Identifiers/Baseline%20visit%20kitID/yes;/studies/UBIOPRED/concepts/Sample%20Identifiers/Bronchoscopy%20visit%20kitID%201/yes;/studies/UBIOPRED/concepts/Sample%20Identifiers/Longitudinal%20visit%20kitID;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Psychiatric%20Disease%20Active/18_or_more;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Psychiatric%20Disease%20Active/2to17;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Psychiatric%20Disease%20Active/unknown;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Osteoporosis%20Active/18_or_more;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Osteoporosis%20Active/less_than_2;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Nasal%20Polyp%20Surgery%20Active/18_or_more;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Nasal%20Polyp%20Surgery%20Active/2to17;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Allergic%20Rhinitis%20Active/no;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Allergic%20Rhinitis%20Active/yes;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Allergic%20Rhinitis%20Age%20Of%20Onset/no;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Allergic%20Rhinitis%20Age%20Of%20Onset/uncertain;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Allergic%20Rhinitis%20Age%20Of%20Onset/yes;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Allergic%20Rhinitis%20Diagnosed/more_than_twice_a_week;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Allergic%20Rhinitis%20Diagnosed/once_a_day;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Allergic%20Rhinitis%20Diagnosed/once_a_month;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Allergic%20Rhinitis%20Diagnosed/weekly;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Congestive%20Diagnosed;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Coronary%20Active/no;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Coronary%20Age%20Of%20Onset/no;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Coronary%20Age%20Of%20Onset/yes;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Coronary%20Diagnosed/no;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Diabetes%20Active;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Diabetes%20Age%20Of%20Onset;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Diabetes%20Diagnosed;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Sinusitis%20Active/Done%20at%20screening%20visit;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Sinusitis%20Active/DONE%20ON%20SAME%20DAY%20AS%20SCREENING;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Sinusitis%20Active/SAME%20DAY%20AS%20SCREENING;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Sinusitis%20Active/SAME%20DAY%20AS%20SCREENING%20VISIT;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Sinusitis%20Active/SCREENING%20AND%20BASELINE%201%20VISIT%20IN%20THE%20SAME%20DAY;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Sinusitis%20Active/THIS%20VISIT%20ON%20SAME%20DAY%20AS%20SCREENING;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Eczema%20Active;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Eczema%20Age%20Of%20Onset/yes;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Eczema%20Diagnosed/null;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Gerd%20Active;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Gerd%20Age%20Of%20Onset;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Gerd%20Diagnosed;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Hay%20Fever%20Active;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Hay%20Fever%20Age%20Of%20Onset;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Hay%20Fever%20Diagnosed;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Psychiatric%20Disease%20Diagnosed/High;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Psychiatric%20Disease%20Diagnosed/med%20to%20low;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Hypertension%20Active;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Hypertension%20Age%20Of%20Onset;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Hypertension%20Diagnosed;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Osteoporosis%20Age%20Of%20Onset/MOMETASONE%2050MCG;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Nasal%20Polyps%20Active;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Nasal%20Polyps%20Age%20Of%20Onset;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Nasal%20Polyps%20Diagnosed;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Nasal%20Polyp%20Surgery%20Age%20Of%20Onset/PLUMBING%20AND%20HEATING%20ENGINEER%20QUALIFICATIONS;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Nasal%20Polyp%20Surgery%20Diagnosed;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Sinus%20Surgery%20Active/no;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Sinusitis%20Age%20Of%20Onset/no;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Sinusitis%20Age%20Of%20Onset/uncertain;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Sinusitis%20Age%20Of%20Onset/yes;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Sinus%20Surgery%20Diagnosed/no;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Sinus%20Surgery%20Diagnosed/uncertain;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Sinus%20Surgery%20Diagnosed/yes;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Vocal%20Chord%20Diagnosed/no;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Vocal%20Chord%20Diagnosed/yes;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Non%20Allergic%20Rhinitis%20Active;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Non%20Allergic%20Rhinitis%20Diagnosed;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Osteoporosis%20Diagnosed;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Psychiatric%20Disease%20Age%20Of%20Onset;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Sinusitis%20Diagnosed;/studies/UBIOPRED/concepts/Subject%20History/Medical%20or%20Surgical%20History/Sinus%20Surgery%20Age%20Of%20Onset;/studies/UBIOPRED/concepts/Subject%20History/Parental%20Hay%20Fever/abnormal_non_clinically_significant;/studies/UBIOPRED/concepts/Subject%20History/Parental%20Hay%20Fever/normal',
            'token': '7b8b0ce3-a2d3-47ca-bc04-2cf4672f44ac'
        }
        annotation = self.run_processor('import:web:transmart:expressions', inputs)
        self.assertFields(annotation, 'expset_type', 'Log2')
        self.assertFileExists(annotation, 'expset')