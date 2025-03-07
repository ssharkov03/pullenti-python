﻿# SDK Pullenti Address, version 4.14, september 2022. Copyright (c) 2013, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

from pullenti.unisharp.Utils import Utils
from pullenti.unisharp.Misc import RefOutArgWrapper

from pullenti.morph.MorphWordForm import MorphWordForm
from pullenti.ner.core.StatisticBigrammInfo import StatisticBigrammInfo
from pullenti.morph.MorphGender import MorphGender
from pullenti.ner.core.StatisticWordInfo import StatisticWordInfo
from pullenti.ner.TextToken import TextToken
from pullenti.ner.core.MiscHelper import MiscHelper

class StatisticCollection:
    """ Статистическая информация о словоформах и их биграммах в тексте - поле AnalysisKit.Statistic.
    Статистика
    """
    
    def __init__(self) -> None:
        self.__m_items = dict()
        self.__m_bigramms = dict()
        self.__m_bigramms_rev = dict()
        self.__m_initials = dict()
        self.__m_initials_rev = dict()
    
    def _prepare(self, first : 'Token') -> None:
        prev = None
        prevt = None
        t = first
        first_pass2831 = True
        while True:
            if first_pass2831: first_pass2831 = False
            else: t = t.next0_
            if (not (t is not None)): break
            if (t.is_hiphen): 
                continue
            it = None
            if (((isinstance(t, TextToken)) and t.chars.is_letter and t.length_char > 1) and not t.chars.is_all_lower): 
                it = self.__add_token(Utils.asObjectOrNull(t, TextToken))
            elif ((((isinstance(t, TextToken)) and t.length_char == 1 and t.chars.is_all_upper) and t.next0_ is not None and t.next0_.is_char('.')) and not t.is_whitespace_after): 
                it = self.__add_token(Utils.asObjectOrNull(t, TextToken))
                t = t.next0_
            if (prev is not None and it is not None): 
                self.__add_bigramm(prev, it)
                if (prevt.chars.equals(t.chars)): 
                    prev.add_after(it)
                    it.add_before(prev)
            prev = it
            prevt = t
        t = first
        while t is not None: 
            if (t.chars.is_letter and (isinstance(t, TextToken))): 
                it = self.__find_item(Utils.asObjectOrNull(t, TextToken), False)
                if (it is not None): 
                    if (t.chars.is_all_lower): 
                        it.lower_count += 1
                    elif (t.chars.is_all_upper): 
                        it.upper_count += 1
                    elif (t.chars.is_capital_upper): 
                        it.capital_count += 1
            t = t.next0_
    
    def __add_token(self, tt : 'TextToken') -> 'StatisticWordInfo':
        vars0_ = list()
        vars0_.append(tt.term)
        s = MiscHelper.get_absolute_normal_value(tt.term, False)
        if (s is not None and not s in vars0_): 
            vars0_.append(s)
        for wff in tt.morph.items: 
            wf = Utils.asObjectOrNull(wff, MorphWordForm)
            if (wf is None): 
                continue
            if (wf.normal_case is not None and not wf.normal_case in vars0_): 
                vars0_.append(wf.normal_case)
            if (wf.normal_full is not None and not wf.normal_full in vars0_): 
                vars0_.append(wf.normal_full)
        res = None
        for v in vars0_: 
            wrapres729 = RefOutArgWrapper(None)
            inoutres730 = Utils.tryGetValue(self.__m_items, v, wrapres729)
            res = wrapres729.value
            if (inoutres730): 
                break
        if (res is None): 
            res = StatisticWordInfo._new731(tt.lemma)
        for v in vars0_: 
            if (not v in self.__m_items): 
                self.__m_items[v] = res
        res.total_count += 1
        if ((isinstance(tt.next0_, TextToken)) and tt.next0_.chars.is_all_lower): 
            if (tt.next0_.chars.is_cyrillic_letter and tt.next0_.get_morph_class_in_dictionary().is_verb): 
                g = tt.next0_.morph.gender
                if (g == MorphGender.FEMINIE): 
                    res.female_verbs_after_count += 1
                elif (((g) & (MorphGender.MASCULINE)) != (MorphGender.UNDEFINED)): 
                    res.male_verbs_after_count += 1
        if (tt.previous is not None): 
            if ((isinstance(tt.previous, TextToken)) and tt.previous.chars.is_letter and not tt.previous.chars.is_all_lower): 
                pass
            else: 
                res.not_capital_before_count += 1
        return res
    
    def __find_item(self, tt : 'TextToken', do_absolute : bool=True) -> 'StatisticWordInfo':
        if (tt is None): 
            return None
        res = None
        wrapres738 = RefOutArgWrapper(None)
        inoutres739 = Utils.tryGetValue(self.__m_items, tt.term, wrapres738)
        res = wrapres738.value
        if (inoutres739): 
            return res
        if (do_absolute): 
            s = MiscHelper.get_absolute_normal_value(tt.term, False)
            if (s is not None): 
                wrapres732 = RefOutArgWrapper(None)
                inoutres733 = Utils.tryGetValue(self.__m_items, s, wrapres732)
                res = wrapres732.value
                if (inoutres733): 
                    return res
        for wff in tt.morph.items: 
            wf = Utils.asObjectOrNull(wff, MorphWordForm)
            if (wf is None): 
                continue
            wrapres736 = RefOutArgWrapper(None)
            inoutres737 = Utils.tryGetValue(self.__m_items, Utils.ifNotNull(wf.normal_case, ""), wrapres736)
            res = wrapres736.value
            if (inoutres737): 
                return res
            wrapres734 = RefOutArgWrapper(None)
            inoutres735 = Utils.tryGetValue(self.__m_items, wf.normal_full, wrapres734)
            res = wrapres734.value
            if (wf.normal_full is not None and inoutres735): 
                return res
        return None
    
    def __add_bigramm(self, b1 : 'StatisticWordInfo', b2 : 'StatisticWordInfo') -> None:
        di = None
        wrapdi742 = RefOutArgWrapper(None)
        inoutres743 = Utils.tryGetValue(self.__m_bigramms, b1.normal, wrapdi742)
        di = wrapdi742.value
        if (not inoutres743): 
            di = dict()
            self.__m_bigramms[b1.normal] = di
        if (b2.normal in di): 
            di[b2.normal] += 1
        else: 
            di[b2.normal] = 1
        wrapdi740 = RefOutArgWrapper(None)
        inoutres741 = Utils.tryGetValue(self.__m_bigramms_rev, b2.normal, wrapdi740)
        di = wrapdi740.value
        if (not inoutres741): 
            di = dict()
            self.__m_bigramms_rev[b2.normal] = di
        if (b1.normal in di): 
            di[b1.normal] += 1
        else: 
            di[b1.normal] = 1
    
    def get_bigramm_info(self, t1 : 'Token', t2 : 'Token') -> 'StatisticBigrammInfo':
        """ Получить статистическую информацию о биграмме токенов
        
        Args:
            t1(Token): первый токен биграммы
            t2(Token): второй токен биграммы
        
        Returns:
            StatisticBigrammInfo: информация о биграмме по всему тексту
        
        """
        si1 = self.__find_item(Utils.asObjectOrNull(t1, TextToken), True)
        si2 = self.__find_item(Utils.asObjectOrNull(t2, TextToken), True)
        if (si1 is None or si2 is None): 
            return None
        return self.__get_bigrams_info(si1, si2)
    
    def __get_bigrams_info(self, si1 : 'StatisticWordInfo', si2 : 'StatisticWordInfo') -> 'StatisticBigrammInfo':
        res = StatisticBigrammInfo._new744(si1.total_count, si2.total_count)
        di12 = None
        wrapdi12746 = RefOutArgWrapper(None)
        Utils.tryGetValue(self.__m_bigramms, si1.normal, wrapdi12746)
        di12 = wrapdi12746.value
        di21 = None
        wrapdi21745 = RefOutArgWrapper(None)
        Utils.tryGetValue(self.__m_bigramms_rev, si2.normal, wrapdi21745)
        di21 = wrapdi21745.value
        if (di12 is not None): 
            if (not si2.normal in di12): 
                res.first_has_other_second = True
            else: 
                res.pair_count = di12[si2.normal]
                if (len(di12) > 1): 
                    res.first_has_other_second = True
        if (di21 is not None): 
            if (not si1.normal in di21): 
                res.second_has_other_first = True
            elif (not si1.normal in di21): 
                res.second_has_other_first = True
            elif (len(di21) > 1): 
                res.second_has_other_first = True
        return res
    
    def get_initial_info(self, ini : str, sur : 'Token') -> 'StatisticBigrammInfo':
        if (Utils.isNullOrEmpty(ini)): 
            return None
        si2 = self.__find_item(Utils.asObjectOrNull(sur, TextToken), True)
        if (si2 is None): 
            return None
        si1 = None
        wrapsi1747 = RefOutArgWrapper(None)
        inoutres748 = Utils.tryGetValue(self.__m_items, ini[0:0+1], wrapsi1747)
        si1 = wrapsi1747.value
        if (not inoutres748): 
            return None
        if (si1 is None): 
            return None
        return self.__get_bigrams_info(si1, si2)
    
    def get_word_info(self, t : 'Token') -> 'StatisticWordInfo':
        """ Получить информацию о словоформе токена
        
        Args:
            t(Token): токен
        
        Returns:
            StatisticWordInfo: статистическая информация по тексту
        
        """
        tt = Utils.asObjectOrNull(t, TextToken)
        if (tt is None): 
            return None
        return self.__find_item(tt, True)